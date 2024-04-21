from enum import Enum
from typing import Union, Type


class DynamicButtons:
    @staticmethod
    async def create(name: str, data: Union[dict[str, str], list[tuple[str, str]]]) -> Type[Enum]:
        return Enum(name, data)
