import asyncio
import logging
import sys
from creds import main
from handlers import commands, inline_keyboards, photos, files, reply_keyboards, polls

# init
dp = main.dp
bot = main.bot


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
