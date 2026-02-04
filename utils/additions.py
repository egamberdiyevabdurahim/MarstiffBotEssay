import os
import string
import pytz

from datetime import datetime


PATTERN = r"^\+?[\d\s]{10,15}$"
BASE62_ALPHABET = string.digits + string.ascii_uppercase + string.ascii_lowercase

ADMIN_LINK = "@MasterPhoneAdmin"
ADMIN_EMAIL = "egamberdiyevabdurahim@gmail.com"

# Setting the base path
# BASE_PATH = os.path.dirname(__file__)
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

tashkent_timezone = pytz.timezone("Asia/Tashkent")
def tas_t():
    return datetime.now(tashkent_timezone)


MESSAGE_EFFECTS = {
    "🔥": "5104841245755180586",
    "👍": "5107584321108051014",
    "❤️": "5159385139981059251",
    "🎉": "5046509860389126442",
    "👎": "5104858069142078462",
    "💩": "5046589136895476101"
}

BOOKING_TIMES = {
    10: ("10:00", "1̶0̶:̶0̶0̶"),
    11: ("11:00", "1̶1̶:̶0̶0̶"),
    14: ("14:00", "1̶4̶:̶0̶0̶"),
    15: ("15:00", "1̶5̶:̶0̶0̶"),
    16: ("16:00", "1̶6̶:̶0̶0̶"),
    17: ("17:00", "1̶7̶:̶0̶0̶"),
    18: ("18:00", "1̶8̶:̶0̶0̶"),
    19: ("19:00", "1̶9̶:̶0̶0̶"),
}


BOOKING_TIMES_CALL = [
    (9, "00"),
    (9, "30"),
    (10, "00"),
    (10, "30"),
    (11, "00"),
    (11, "30"),
    (14, "00"),
    (14, "30"),
    (15, "00"),
    (15, "30"),
    (16, "00"),
    (16, "30"),
    (17, "00"),
    (17, "30"),
    (18, "00"),
    (18, "30"),
    (19, "00"),
    (19, "30"),
]