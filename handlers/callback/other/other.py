from aiogram import Router
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from service.loggerSerice.settings_logger import logger

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter())
async def any_callback(callback: CallbackQuery, callback_data: UserCallbackFactory) -> None:
    logger.info(callback_data)