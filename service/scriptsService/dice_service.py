import random


class DiceService:
    @staticmethod
    async def random_dice(facets: int) -> int:
        return random.randint(1, facets)
