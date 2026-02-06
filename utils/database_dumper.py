import os
import subprocess
from aiogram.types import FSInputFile
from database_config.config import (
    DB_USER, DB_NAME, DB_HOST, DB_PORT, DB_PASS, DEVELOPERS_GROUP_ID
)
from loader import bot
from utils.notifier import notice_developer
from utils.additions import BASE_PATH, tas_t

DUMP_PATH = f"{BASE_PATH}/database.sql"
ENCRYPTED_PATH = f"{BASE_PATH}/database.sql.7z"

async def send_dump_to_telegram():
    """Send the ENCRYPTED database dump to Telegram."""
    if os.path.exists(ENCRYPTED_PATH):
        document = FSInputFile(ENCRYPTED_PATH)
        caption = (
            f"🔐 Encrypted Backup\n"
            f"Date: {tas_t().strftime('%Y-%m-%d %H:%M')}\n"
            f"⚠️ Decrypt with 7z + BACKUP_PASSWORD"
        )
        try:
            await bot.send_document(
                chat_id=DEVELOPERS_GROUP_ID,
                document=document,
                caption=caption,
                message_thread_id=2,
            )
        except Exception as e:
            await notice_developer(message=f"Failed to send encrypted dump: {str(e)}")
        finally:
            # Clean up BOTH files
            if os.path.exists(DUMP_PATH):
                os.remove(DUMP_PATH)
            if os.path.exists(ENCRYPTED_PATH):
                os.remove(ENCRYPTED_PATH)
    else:
        await notice_developer(message="Encrypted dump file does not exist")

async def dump_and_send():
    """Dump → Encrypt with 7z → Send to Telegram."""
    password = os.getenv("BACKUP_PASSWORD")
    if not password:
        await notice_developer(message="BACKUP_PASSWORD not set in .env!")
        return

    try:
        # Ensure base path exists
        os.makedirs(BASE_PATH, exist_ok=True)

        # Step 1: Dump database (plain SQL)
        dump_command = f"pg_dump -U {DB_USER} -h {DB_HOST} -p {DB_PORT} -F p -d {DB_NAME} -f {DUMP_PATH}"
        env = os.environ.copy()
        env["PGPASSWORD"] = DB_PASS
        subprocess.run(dump_command, shell=True, check=True, env=env)

        # Step 2: Encrypt with 7z (AES-256)
        # -mhe=on → encrypts filenames/headers too (critical for security)
        encrypt_command = [
            "7z", "a",
            "-t7z",          # 7z format
            "-m0=lzma2",     # Compression method
            "-mx=9",         # Max compression
            f"-p{password}", # Password (from env var)
            "-mhe=on",       # Encrypt headers (hides table names!)
            ENCRYPTED_PATH,
            DUMP_PATH
        ]
        subprocess.run(encrypt_command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Step 3: Send encrypted file
        await send_dump_to_telegram()

    except subprocess.CalledProcessError as e:
        await notice_developer(message=f"Backup failed: {str(e)}")
    except Exception as e:
        await notice_developer(message=f"Unexpected error: {str(e)}")
    finally:
        # Always clean up plain SQL (security first!)
        if os.path.exists(DUMP_PATH):
            os.remove(DUMP_PATH)
        if os.path.exists(ENCRYPTED_PATH):
            os.remove(ENCRYPTED_PATH)
