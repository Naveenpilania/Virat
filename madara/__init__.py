from telethon import TelegramClient
import logging
import time

openai_key ="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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5794992821:AAFUF1v7_g7ySdsdUz2Hh9jWR1czLWRWRc4"

bot = TelegramClient(("amit_bot"), api_id, api_hash).start(bot_token = bot_token)