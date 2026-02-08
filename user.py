from config import Config
from config import LOGGER
from pyrogram import Client
from pyrogram.session.string_session import StringSession

BOT_USERNAME = Config.BOT_USERNAME


class User(Client):
    def __init__(self):
        super().__init__(
            session=StringSession(Config.SESSION),
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
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
        
