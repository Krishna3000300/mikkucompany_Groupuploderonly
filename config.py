import os

API_ID = API_ID = 24932120

API_HASH = os.environ.get("API_HASH", "b16b8704b5c839ed24f4ed5824978a3b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7241359123:AAEfrhbTDJ_YfdqzqELyFeI-0R6duWR-AFQ")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6907400500))

LOG = -1002054181760

try:
    ADMINS=[7045457279]
    for x in (os.environ.get("ADMINS", "7045457279").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


