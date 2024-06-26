from glob import glob
from importlib import import_module
from os.path import join

from aiogram import Dispatcher

from service.loggerSerice.settings_logger import logger


class LoadService:
    @staticmethod
    async def load_router(dp: Dispatcher, handlers_dir: str = "handlers") -> None:
        """Подключает все роутеры находящиеся в папке handlers(по умолчанию)(работает и с вложенными папками).

        Args:
            handlers_dir (str):  The main folder where the routers are located. Defaults to 'handlers'.
            dp (Dispatcher): module from aiogram
        Returns:
            None

        """

        def custom_sort(line: str) -> int:
            if "admin" in line and "error" not in line:
                return 0
            elif "user" in line and "error" not in line:
                return 1
            elif "error" in line:
                return 2
            else:
                return 3

        modules = [
            module.replace("/", ".").replace(".py", "")
            for module in map(
                lambda item: item.replace("\\", "/"),
                glob(join(handlers_dir, "**", "*.py"), recursive=True),
            )
        ]
        modules.sort(key=custom_sort)
        for index, module in enumerate(modules, start=1):
            module_name = import_module(module)
            if hasattr(module_name, "router"):
                router = getattr(module_name, "router")
                dp.include_router(router)
                logger.debug(f"#{index} Success add handler {module}!")
        logger.info("All handler have been loaded.")

    @staticmethod
    async def load_middlewares(
            dp: Dispatcher, middlewares_dir: str = "middlewares"
    ) -> None:
        """
        Подключает все мидлвари находящиеся в папке middlewares(по умолчанию)(работает и с вложенными папками).

        Args:
            middlewares_dir (str):  The main folder where the routers are located. Defaults to 'middlewares'.
            dp (Dispatcher): module from aiogram
        Returns:
            None
        """
        modules = [
            module.replace("/", ".").replace(".py", "")
            for module in map(
                lambda item: item.replace("\\", "/"),
                glob(join(middlewares_dir, "*.py")),
            )
        ]
        for module in modules:
            module_name = import_module(module)
            # Разбираем название модуля по точкам, чтобы найти часть с названием класса middleware
            module_attributes = dir(module_name)
            # Ищем классы, название которых содержит "Middleware"
            middleware_classes = [
                attr
                for attr in module_attributes
                if "Middleware" in attr and attr != "BaseMiddleware"
            ]
            for middleware_class in middleware_classes:
                # Получаем объект класса middleware
                middleware = getattr(module_name, middleware_class)
                # Подключаем middleware к соответствующему хендлеру
                if "callback" in module:
                    dp.callback_query.outer_middleware(middleware())
                    logger.debug(f"Success add middleware {module} in callback!")
                elif "message" in module:
                    dp.message.outer_middleware(middleware())
                    logger.debug(f"Success add middleware {module} in message!")
        logger.info("All middlewares have been loaded.")
