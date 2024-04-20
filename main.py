import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.middlewares.request_logging import RequestLogging
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods import GetUpdates
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config.config import load_config
from config.main_commands import load_main_commands
from service.botSerivce.load_handlers import LoadService
from service.loggerSerice.settings_logger import logger


async def main():
    bot_properties: DefaultBotProperties = DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )

    storge: MemoryStorage = MemoryStorage()
    bot: Bot = Bot(token=load_config().Telegram.BotToken, default=bot_properties)
    scheduler: AsyncIOScheduler = AsyncIOScheduler(timezone="Asia/Yekaterinburg")
    dp: Dispatcher = Dispatcher(storge=storge, scheduler=scheduler)

    bot.session.middleware(RequestLogging(ignore_methods=[GetUpdates]))

    await LoadService.load_router(dp=dp)
    await load_main_commands(bot=bot)

    logger.info("Starting bot!")
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
