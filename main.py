import asyncio

from program import LOGS
from pytgcalls import run
from driver.core import calls, bot, user


async def start_bot():
    await bot.start()
    LOGS.info("[INFO]: BOT & USERBOT CLIENT STARTED !!")
    await calls.start()
    LOGS.info("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("VeezSupportGroup")
    await user.join_chat("levinachannel")
    await run()
    LOGS.info("[INFO]: BOT & USERBOT STARTED !!")
    await bot.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
