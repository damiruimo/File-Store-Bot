import os

API_ID = int(os.environ.get("API_ID", "29911491"))
API_HASH = os.environ.get("API_HASH", "e249436d7295d1a151809fc5391fee9d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8494273359:AAF3Jlh231CjnKazgDDPzru-KSzrRuVba70")
STORAGE_CHANNEL = int(os.environ.get("STORAGE_CHANNEL", "-1003511585157"))

if not all([API_ID, API_HASH, BOT_TOKEN, STORAGE_CHANNEL]):
    raise RuntimeError("❌ Missing environment variables")
