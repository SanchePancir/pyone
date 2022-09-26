import telebot
import logging
from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

owm = OWM('90da11b50b80f3c5cb460472d027a323')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('api', config_dict)
bot = telebot.TeleBot("5249995039:AAHbvgAErJPdju20QvqWOU4rCG2qDY0XSdo")


@client.message_handler(commands=['help'])
def start_bot(message):
    help_comm = "Для того чтобы узнать погоду в том или ином городе введите его название.\nВАЖНО пиши названия городов правильно, а то я могу отключиться🤒"
    client.send_message(message.chat.id,help_comm)

@client.message_handler(commands=['start'])
def start_bot(message):
    start = f"<b>Добро Пожаловать {message.from_user.first_name}!</b>\n Для того чтобы узнать погоду в том или ином городе введите его название:"
    client.send_message(message.chat.id,start,parse_mode='html')

@client.message_handler(content_types=['text'])
def send_answer(message):
    try:
        observation = mgr.weather_at_place("") 
    except NotFoundError: 
        print('error NotfoundError') 
        mute = ()
    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
    except NotFoundError:
        mute = ("Хм такого города не существует")
    w.wind()
    w.humidity
    temp = w.temperature('celsius')['temp']

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
    answer += "Температура сейчас " + str(temp) + "°C." + "\n\n"

    if temp < -5:
        answer += "На улице сильный мороз, одевайся тепло 🥶"
    elif temp < 0:
        answer+="На улице мороз, одевайся тепло 🥶."
    elif temp < 10:
        answer+="Как-то прохладно, одевайся потеплее 🙂."
    elif temp < 17:
        answer+= "Температура приемлимая, но одеться стоит 😊."
    else:
        answer+= "Температура отличная одевайся во что хочешь 😉."
    client.send_message(message.chat.id,answer)


if __name__ == '__main__':
    client.polling( none_stop = True )

