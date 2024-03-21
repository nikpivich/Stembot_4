import asyncio
import logging

from aiogram.client.default import DefaultBotProperties

import config
from aiogram import Bot, Dispatcher
from handlers import questions, base,gen_image, no_handler, test, games
from aiogram.enums.parse_mode import ParseMode



async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()


    dp.include_routers(base.router,
                       questions.router,
                       gen_image.router,
                       test.router,
                       games.router,
                       no_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())