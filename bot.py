import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, STORAGE_CHANNEL

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Client(
    "file-store-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message: Message):
    await message.reply_text(
        "📦 **Telegram File Store Bot**\n\n"
        "Send me any file and I will store it safely.\n"
        "You’ll get a permanent download link 🔗"
    )

@app.on_message(filters.private & filters.media)
async def store_file(client, message: Message):
    try:
        sent = await message.copy(STORAGE_CHANNEL)

        channel_id = str(STORAGE_CHANNEL).replace("-100", "")
        file_link = f"https://t.me/c/{channel_id}/{sent.id}"

        await message.reply_text(
            "✅ **File Stored Successfully!**\n\n"
            f"🔗 **Download Link:**\n{file_link}"
        )

    except Exception as e:
        logging.error(e)
        await message.reply_text("❌ Failed to store file. Try again.")

@app.on_message(filters.private)
async def unsupported(client, message: Message):
    await message.reply_text("⚠️ Please send a valid file or media.")

app.run()
