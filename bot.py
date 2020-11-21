#!/usr/bin/python3
from dotenv import load_dotenv
from src.modules.discord_bot import DiscordBot
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Reading env configuration")
    load_dotenv()
    bot = DiscordBot()
    bot.start()

