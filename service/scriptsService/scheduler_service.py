from apscheduler.job import Job


class SchedulerService:
    @staticmethod
    async def current_data(all_scheduler: list[Job], user_scheduler: list[Job]) -> list:
        return list(filter(lambda job: job in all_scheduler, user_scheduler))
