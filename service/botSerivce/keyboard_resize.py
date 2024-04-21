class KeyboardResize:
    @staticmethod
    async def two_one(count_main_buttons: int, count_any_buttons: int = 1) -> tuple[int]:
        result_size = list()
        for index in range(count_main_buttons):
            if index % 3 == 1:
                result_size.append(2)
            elif index % 3 == 2:
                result_size.append(1)
        return tuple(result_size + [1] * count_any_buttons)
