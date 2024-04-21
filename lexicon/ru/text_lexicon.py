class Default:
    backName: str = "Вернуться 🔚"


class MessageText:
    anyMessage: str = "Я получил сообщение <b>{userMessage}</b>"
    start: str = "Вас приветствует <b>Yandex-Lyceum-bot</b> 👋!"
    timer: str = "⏲ <i>Выберите нужный таймер</i>"
    dice: str = "<b><i>Выпало число <code>{number}</code> 🎲</i></b>"
    double_dice: str = "{first} и {second}"
    get_city: str = """
<i>Пройдите небольшой опрос, пожалуйста!</i>
<b>В каком городе вы проживаете?</b>"""
    get_weather: str = """<b>А какая в Вашем городе погода?</b>"""
    end_survey: str = """
<b><i>✅ Вы успешно прошли опросник! ✅
Спасибо! 🍭</i></b>"""
    stop_survey: str = """<i><b>Вы успешно отменили опросник!✅</b></i>"""


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
