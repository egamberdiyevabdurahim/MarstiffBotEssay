from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.i18n import I18n

from database_config.config import TOKEN
from models import (
    user, history, errors, balance, transaction,
    essentials, tg_group, tg_group_section, event, event_user,
    essay, essay_user,
)

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

i18n = I18n(path="locales", default_locale="en", domain="lang")
_ = i18n.gettext

# MODELS
User = user.UserModel

Event = event.EventModel
EventUser = event_user.EventUserModel
Essay = essay.EssayModel
EssayUser = essay_user.EssayUserModel

History = history.HistoryModel
Errors = errors.ErrorsModel

Essentials = essentials.EssentialsModel
TGGroup = tg_group.TGGroupModel
TGGroupSection = tg_group_section.TGGroupSectionModel

# Finance & Management (NEW)
Balance = balance.BalanceModel
Transaction = transaction.TransactionModel
