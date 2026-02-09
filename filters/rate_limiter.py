import time
import asyncio
import logging

from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject, Message, CallbackQuery, User
from typing import Callable, Dict, Any, Awaitable, List
from collections import defaultdict

from database_config.config import ADMINISTRATION_GROUP_ID


class RateLimiter(BaseMiddleware):
    """
    Per-user rate limiting with admin alerts for abusive behavior.

    Default limits:
    - Regular commands: 4 requests / 5 seconds
    - Heavy operations (booking/payment): 1 request / 10 seconds

    Abuse detection:
    - Notify admin if user hits rate limit 5+ times within 60 seconds
    """

    def __init__(self, bot: Bot):
        self.bot = bot
        self.windows: Dict[int, Dict[float, int]] = defaultdict(dict)
        self.abuse_windows: Dict[int, List[float]] = defaultdict(list)
        self.notified_users: Dict[int, float] = {}
        self.lock = asyncio.Lock()

        # Configurable limits
        self.default_limit = 4
        self.default_window = 5.0
        self.heavy_limit = 1
        self.heavy_window = 10.0
        self.abuse_threshold = 5
        self.abuse_window = 60.0
        self.notification_cooldown = 300.0

    def _is_heavy_operation(self, event: TelegramObject) -> bool:
        """Detect actual heavy DB operations in YOUR bot"""
        if isinstance(event, CallbackQuery):
            data = event.data or ""
            # Only these are truly heavy (DB writes + admin notifications)
            return any(k in data for k in ["book_essay", "participate_event:", "accept_", "decline_"])
        return False

    def _cleanup_windows(self, current_time: float):
        """Clean expired windows to prevent memory leaks"""
        # Clean request windows
        for user_id in list(self.windows.keys()):
            expired = [ts for ts in self.windows[user_id]
                       if current_time - ts > max(self.default_window, self.heavy_window)]
            for ts in expired:
                del self.windows[user_id][ts]
            if not self.windows[user_id]:
                del self.windows[user_id]

        # Clean abuse windows
        for user_id in list(self.abuse_windows.keys()):
            self.abuse_windows[user_id] = [
                ts for ts in self.abuse_windows[user_id]
                if current_time - ts <= self.abuse_window
            ]
            if not self.abuse_windows[user_id]:
                del self.abuse_windows[user_id]

        # Clean notification cooldowns
        for user_id in list(self.notified_users.keys()):
            if current_time - self.notified_users[user_id] > self.notification_cooldown:
                del self.notified_users[user_id]

    async def _notify_admin(self, user: User, abuse_count: int):
        """Send non-blocking admin notification about abusive user"""
        try:
            user_info = (
                f"⚠️ <b>Abusive User Detected</b>\n\n"
                f"📱 User: <a href='tg://user?id={user.id}'>{user.full_name or 'Unknown'}</a> "
                f"(@{user.username or 'no_username'})\n"
                f"🆔 ID: <code>{user.id}</code>\n"
                f"🚨 Rate limited {abuse_count} times in {self.abuse_window} seconds\n"
                f"⏱️ {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"
            )

            # Fire-and-forget with timeout
            asyncio.create_task(
                asyncio.wait_for(
                    self.bot.send_message(
                        chat_id=ADMINISTRATION_GROUP_ID,
                        text=user_info,
                        parse_mode="HTML",
                        message_thread_id=5
                    ),
                    timeout=5.0
                )
            )
            logging.warning(f"Abuse alert sent for user={user.id} (hits={abuse_count})")
        except Exception as e:
            logging.error(f"Failed to send abuse alert: {e}")

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]  # ✅ FIXED: Added parameter name
    ) -> Any:
        # Skip non-user events
        user_obj = data.get("event_from_user")
        if not user_obj or not isinstance(user_obj, User):
            return await handler(event, data)

        user_id = user_obj.id
        current_time = time.time()

        # Determine limits
        # is_heavy = self._is_heavy_operation(event)
        # limit = self.heavy_limit if is_heavy else self.default_limit
        # window = self.heavy_window if is_heavy else self.default_window
        limit = self.default_limit
        window =  self.default_window

        async with self.lock:
            self._cleanup_windows(current_time)

            # Count requests in current window
            if user_id in self.windows:
                request_count = sum(
                    count for ts, count in self.windows[user_id].items()
                    if current_time - ts <= window
                )
            else:
                request_count = 0

            # ⚠️ RATE LIMITED?
            if request_count >= limit:
                # Record abuse event
                self.abuse_windows[user_id].append(current_time)

                # Check for abuse pattern
                recent_abuse = [
                    ts for ts in self.abuse_windows[user_id]
                    if current_time - ts <= self.abuse_window
                ]
                abuse_count = len(recent_abuse)

                if abuse_count >= self.abuse_threshold and user_id not in self.notified_users:
                    self.notified_users[user_id] = current_time
                    asyncio.create_task(self._notify_admin(user_obj, abuse_count))

                # Calculate retry time (✅ FIXED: handle empty window safely)
                if user_id in self.windows and self.windows[user_id]:
                    oldest_ts = min(self.windows[user_id].keys())
                    retry_after = max(1, int(window - (current_time - oldest_ts)))
                else:
                    retry_after = int(window)

                # Send user feedback
                if isinstance(event, Message):
                    await event.answer(
                        f"⏳ Пожалуйста, подождите {retry_after} секунд перед следующим действием.\n"
                        f"Это помогает боту работать быстрее для всех студентов! 🚀"
                    )
                elif isinstance(event, CallbackQuery):
                    await event.answer(
                        f"Подождите {retry_after} секунд ⏳",
                        show_alert=True
                    )

                return None  # ✅ BLOCK request HERE

            # ✅ REGISTER successful request (MOVED OUTSIDE rate-limit block)
            self.windows[user_id][current_time] = 1

        # ✅ Allow handler to proceed (MOVED OUTSIDE lock block for better concurrency)
        return await handler(event, data)