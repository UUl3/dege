## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCI2MlvbWqUAAMkjIf2FyIxXVjRRzKbJ_dHfMwpdyFHMtL3IS4QBJ0ggwZO6KoWqYHzdZ2Re4LCvVI1YL6kVhYS3HzNJJk63KWGq75ddvrfzBGtFhSH1340NxPR4mpRlPHezbCz9MywLLmzalTzrxKN5s5iCD03XYI2us3wpec-oos0iTUeFu4gp5mmiN24YXLT8xXqJiQNIWmHgTJhaCTRPQDOj8UP9gQZBhaasdzcrdYExNesqiuLkHXntQEfw6cxiOuMbW1zvvPTk2dLW7g-xByQr2kNockij8S_dJLRtlHDm7kTqH5WlbNHvXovbzaYzkj7OziSPt5Ktw7HpFYlAAAAATqF9iEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5510979902:AAGJqvBZ4Xg-2Ubu9-yQePL2b3FrkmSBDkQ")
BOT_NAME = getenv("BOT_NAME", "ꞏ𝙵𝙰𝚁𝙰𝚆𝙻𝙰 ｢♥️｣")
API_ID = int(getenv("API_ID", "16234465"))
API_HASH = getenv("API_HASH", "8e67f77b5527aa5dbedd7d283e6199b5")
OWNER_NAME = getenv("OWNER_NAME", "𝑇 𝑂 𝑋 𝐼 𝐶")
OWNER_USERNAME = getenv("OWNER_USERNAME", "YUX0O")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "YUU_Qbot")
OWNER_ID = getenv("OWNER_ID", "5276825121")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "YUX0O")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "U_X_B_F")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Ullillil")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split(.))
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
