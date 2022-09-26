import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('90da11b50b80f3c5cb460472d027a323', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("5249995039:AAHbvgAErJPdju20QvqWOU4rCG2qDY0XSdo")
@bot.message_handler(func=lambda m: True)

def echo_all(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура в райне " + str(temp) + "°C" + "\n\n"

	if temp < 10:
    	    answer +="Пиздец как холодно! Одевайся как чёрт!"
	elif temp < 20:
    	    answer += "В данный момент прохладненько, пора разчехлять кофточку, а может сразу две!"
	else:
    	    answer +="Погода огонь, цепляй маечку и поглани кутить!"
	
	bot.reply_to(message, answer)
	
bot.polling( none_stop = True)