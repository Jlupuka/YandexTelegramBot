from enum import Enum


class AnyMessage:
    anyMessage: str = "Я получил сообщение <b>{userMessage}</b>"


class CommandText:
    nowTime: str = "<i>Время сейчас - <code>{nowTime}</code></i>"
    nowDate: str = "<i>Сегодняшняя дата - <code>{nowDate}</code></i>"
    setTimer: str = "<i>Таймер сработал через - <code>{sleepTime}</code> секунд</i>"


class MainCommands(Enum):
    time: str = "Узнать нынешнее время"
    date: str = "Узнать нынешнюю дату"
    set_timer: str = "Установить таймер"


class ErrorText:
    rangeTimer: str = "🔴 <b><i>Вы вышли из диапазона возможности таймера!</i></b> 🔴"
    typeTimer: str = """
🔴 <b><i>Вы ввели некорректный формат данных</i></b> 🔴
Пример правильного формата: <code>/set_timer 23</code>"""
