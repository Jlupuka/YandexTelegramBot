from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from service.loggerSerice.settings_logger import logger

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter())
async def any_callback(callback: CallbackQuery, callback_data: UserCallbackFactory, state: FSMContext) -> None:
    logger.info(f"{callback_data}, {await state.get_state()}")
