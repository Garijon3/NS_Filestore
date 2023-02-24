import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client
API_ID = int(os.environ.get("API_ID", "26364421"))
API_HASH = os.environ.get("API_HASH", "72c7598f883fa1b077358d6c86071654")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047825180:AAHxFJdl2C7MdBr98Q-f-vCH1dHUTlwvnak")


def main():
    plugins = dict(root="plugins")
    app = Client("FileStore",
                 bot_token=BOT_TOKEN,
                 api_id=API_ID,
                 api_hash=API_HASH,
                 plugins=plugins,
                 workers=100)

    app.run()


if __name__ == "__main__":
    main()
