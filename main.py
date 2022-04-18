import asyncio
from pyrogram import Client

api_id = 13169928
api_hash = 'a41b48c9f67965cf8b621e3046bb06dc'


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("autist_mylive", "Greetings from **Pyrogram**!")

asyncio.run(main())
