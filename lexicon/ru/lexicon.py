from enum import Enum


class AnyMessage:
    anyMessage: str = "Я получил сообщение <b>{userMessage}</b>"


class CommandText:
    nowTime: str = "Время сейчас - <code>{nowTime}</code>"
    nowDate: str = "Сегодняшняя дата - <code>{nowDate}</code>"


class MainCommands(Enum):
    time: str = "Узнать нынешнее время"
    date: str = "Узнать нынешнюю дату"
