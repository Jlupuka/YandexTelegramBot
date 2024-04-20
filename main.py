import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.methods import GetUpdates
from aiogram.client.session.middlewares.request_logging import RequestLogging

import service.botSerivce.load_handlers
from config.config import load_config
from service.loggerSerice.settings_logger import logger


async def main():
    bot_properties: DefaultBotProperties = DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )

    bot: Bot = Bot(token=load_config().Telegram.BotToken, default=bot_properties)
    dp: Dispatcher = Dispatcher()

    bot.session.middleware(RequestLogging(ignore_methods=[GetUpdates]))

    await service.botSerivce.load_handlers.LoadService.load_router(dp=dp)

    logger.info("Starting bot!")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
