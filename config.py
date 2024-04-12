from os import getenv

from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("TOKEN", "7085860807:AAGgnnMH092foEtejPVkgpy0xGXrFM0T_8k")
"Telegram bot token obtained from botfather"
DB_URI = getenv("MONGO_URL")
"database url (mongo)"
OWNER_ID = "5631563685"
"Telegram ID of the bot owner"
LOGGER_ID = int(getenv("LOGGER_ID", None))
"channel/group ID with `-` for keeping track of new errors where the bot gets..."
SUDO_USER = list(map(int, getenv("SUDO_USER", "").split()))
"set of user ID which can have elevated privileges"
LOGGER_LEVEL = getenv("LOGGER_LEVEL", 20)
"logger level, `debug(10)`, `info(20)`, `warn(30)` and `error(40)`. default is `info`"

TIME_ZONE = "Asia/Kolkata"
