import datetime


class TimeService:
    @staticmethod
    async def now_date() -> str:
        return datetime.datetime.strftime(datetime.datetime.now(), "%d-%m-%Y")

    @staticmethod
    async def now_time() -> str:
        return datetime.datetime.strftime(datetime.datetime.now(), "%H:%M")

    @staticmethod
    async def add_time(time: float) -> datetime:
        return datetime.datetime.now() + datetime.timedelta(seconds=time)

