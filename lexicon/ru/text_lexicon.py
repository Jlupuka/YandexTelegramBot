class Default:
    backName: str = "Вернуться 🔚"


class MessageText:
    anyMessage: str = "Я получил сообщение <b>{userMessage}</b>"
    start: str = "Вас приветствует <b>Yandex-Lyceum-bot</b> 👋!"
    timer: str = "⏲ <i>Выберите нужный таймер</i>"
    dice: str = "<b><i>Выпало число <code>{number}</code> 🎲</i></b>"
    double_dice: str = "{first} и {second}"


class CommandText:
    nowTime: str = "🕰 <i>Время сейчас ⟶ <code>{nowTime}</code></i>"
    nowDate: str = "📅 <i>Сегодняшняя дата ⟶ <code>{nowDate}</code></i>"
    setTimer: str = "<i><code>{sleepTime}</code> - засек! 🟣</i>"
    completedTimer: str = "<i><code>{sleepTime}</code> - истекло! ✅</i>"
    close: str = "<b>Все таймеры были успешно сброшены! ✅</b>"


class ErrorText:
    rangeTimer: str = "🔴 <b><i>Вы вышли из диапазона возможности таймера!</i></b> 🔴"
    typeTimer: str = """
🔴 <b><i>Вы ввели некорректный формат данных</i></b> 🔴
Пример правильного формата: <code>/set_timer 23</code>"""
    emptyTimer: str = """
🔴 <b><i>У вас нет никаких активных таймеров!</i></b> 🔴"""
