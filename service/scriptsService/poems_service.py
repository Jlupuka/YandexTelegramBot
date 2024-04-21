import asyncio
import json
from enum import Enum
from typing import Any, Type

import aiofiles

from service.botSerivce.create_dynamic_buttons import DynamicButtons


class PoemsService:
    @staticmethod
    async def poems_data() -> dict[str: dict[str]]:
        async with aiofiles.open(file="src/data/poems.json", mode="r", encoding="utf-8") as file:
            return json.loads(await file.read())

    @staticmethod
    async def authors() -> tuple[Any, ...]:
        return tuple(author for author in (await PoemsService.poems_data()).keys())

    @staticmethod
    async def author_works(author: str) -> dict[str]:
        return (await PoemsService.poems_data())[author]

    @staticmethod
    async def poem(author: str, poem_name: str) -> str:
        return (await PoemsService.author_works(author=author))[poem_name]

    @staticmethod
    async def authors_for_button() -> Type[Enum]:
        return await DynamicButtons.create("Authors", [(f"author_{index}", author) for index, author in
                                                       enumerate(await PoemsService.authors())])

    @staticmethod
    async def poems_for_button(author: str) -> Type[Enum]:
        return await DynamicButtons.create("Poems", [(f"poem_{index}", author) for index, author in
                                                     enumerate(await PoemsService.author_works(author=author))])


if __name__ == "__main__":
    print(asyncio.run(PoemsService.poem("А.С.Пушкин", "Бородино")))
