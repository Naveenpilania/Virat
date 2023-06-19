from telethon import TelegramClient
import logging
import time

openai_key ="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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6267708263:AAFUp5DRNjJt4mkTKQXZFdZnTqm8MN12i24"

bot = TelegramClient(("virat_bot"), api_id, api_hash).start(bot_token = bot_token)