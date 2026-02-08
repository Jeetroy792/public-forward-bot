from pyrogram import Client, __version__

from config import Config
from config import LOGGER

from user import User
import pyromod.listen
import os
import time
from pyrogram import Client

# সেশন স্টার্ট করার ঠিক আগে এটি যোগ করে দেখতে পারেন
# যদি পাইগ্রামের ইন্টারনাল অফসেট কাজ না করে তবে এটি সার্ভার ভেদে সমস্যা করে




class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=10,
            bot_token=Config.BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()

        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} started!"
        )

        # ✅ USER SESSION ONLY IF SESSION EXISTS
        if Config.SESSION:
            self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
