from config import Config
from config import LOGGER
from pyrogram import Client

BOT_USERNAME = Config.BOT_USERNAME


class User(Client):
    def __init__(self):
        super().__init__(
            name="user",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.SESSION,   # ✅ Pyrogram v1 compatible
            workers=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        if BOT_USERNAME:
            await self.send_message(chat_id=BOT_USERNAME, text="/forward")
        me = await self.get_me()
        return self, me.id

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
