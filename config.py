import os

API_ID = API_ID = 24119778

API_HASH = os.environ.get("API_HASH", "cca11ca97dd8683d65ca1beb62baceb1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6447790495:AAFzsUymnAsQVSGYmoeEGFu4lbB1gqj7rso")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1991641730))

LOG = -1002054181760

try:
    ADMINS=[7045457279]
    for x in (os.environ.get("ADMINS", "7045457279").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


