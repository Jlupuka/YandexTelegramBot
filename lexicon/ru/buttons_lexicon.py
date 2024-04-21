from enum import Enum


class StartButtons(Enum):
    dice: str = "Dice 🎲"
    timer: str = "Таймер 🕘"
    survey: str = "Пройти опрос ❓"


class DiceButtons(Enum):
    hexagonal: str = "Шестигранный 🎲"
    double_hexagonal: str = "Шестигранный х2 🎲"
    twenty_sided: str = "20-гранный 🎲"


class TimerButtons(Enum):
    seconds_30: str = "30 секунд"
    one_minute: str = "1 минута"
    five_minute: str = "5 минут"


class MainCommands(Enum):
    start: str = "Начать работу с ботом"
    time: str = "Узнать нынешнее время"
    date: str = "Узнать нынешнюю дату"
    set_timer: str = "Установить таймер"
    close: str = "Остановить все таймеры"
    stop: str = "Остановить опросник"
    

class SkipSurvey(Enum):
    skip_get_city: str = "Пропустить ➡️"
