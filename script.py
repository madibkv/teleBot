from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackContext
import logging
import random
import datetime,pytz


updater = Updater(token='5122698218:AAFWpy_RooKtfQkGDL2Jlw9tKM1dC9e2MQM', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

CURRENT_VERSION = 'modiBot v3.0'
GOOD_NIGHT_MSGS = ['Спокойной ночи', 'Спокойной ночи, лю тя', 'Спокойной бро, лю тя', 'Спокойной ночи бро, лублу тя','лубу тебя, спокойной ночи',
'Спокойной ночи бро', 'Спокойной бро, лю тебя', 'Спи крепко бро, лублу тебя','Спокойной ночи, лублу тя','Спокойной, лу тя бро']

SECRET_MSG = """Хоба! Тебе выпало секретное сообщение! Шанс выпадения всего
3%!!!

В этом сообщении бро, хошу сказать тебе спасибо. Спасибо тебе за твою доброту и заботу, за то шо уделяешь мне время, проявляешь внимание, поднимаешь мне настроение, за то шо нравлюсь тебе таким какой я есть. 
А также за все те маленькие жесты шо ты для меня делаешь. Как за твой подарок в виде эко еды перед отлетом, или за духи что ты дала мне в дорогу, за нашу фотку которую ты позволила мне оставить себе, за те твои угощения в Куликовском, или за то шо приготовила мне самую вкусную пасту тогда у Рахата дома. За то что терпишь мои холодные руки 😂😂😂 
И еще за многое многое другое.
Все эти вещи для меня очень много значат и я их очень ценю. Спасибо за то шо каждый день делаешь мою жизнь чуточку лучше. Спасибо тебе за то, что ты есть
Лю тебя и очень по тебе скучаю! 
Спокойной ночи бро :)"""



def start(update, context):
	message = 'Халооооу'
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)
	#user_id = update.message.from_user.id
	#print(user_id)

def check_current_version(update, context):
	message = CURRENT_VERSION
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def send_secret_message(update, context):
	message = SECRET_MSG
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def reply(update,context):
	message = '♥'
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)
	context.bot.send_message(chat_id=256346230,text=update.message.text)

def good_night(context : CallbackContext):
	message = random.choice(GOOD_NIGHT_MSGS)
	chance = random.randint(1,100)
	if chance == 7 or chance == 33 or chance == 77 or chance == 55 or chance == 25:
		message = SECRET_MSG

	debug_msg = message + '\n\nRandint: '+str(chance)

	context.bot.send_message(chat_id=256346230,text=debug_msg)
	context.bot.send_message(chat_id=724989540,text=message)

	
def count_down(update, context):
	delta = datetime.datetime(year=2022,month=6,day=17,hour=9,minute=45) - datetime.datetime.now()
	seconds = delta.seconds

	days = delta.days
	hours = seconds//3600
	minutes = seconds%3600//60

	#lang = update_language(days,hours,minutes)

	message = 'Осталось: '+str(days)+'д '+ str(hours) + 'ч '+ str(minutes) + 'м'
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)


# 724989540

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

version_handler = CommandHandler('version',check_current_version)
dispatcher.add_handler(version_handler)

secret_handler = CommandHandler('secret',send_secret_message)
dispatcher.add_handler(secret_handler)

countdown_handler = CommandHandler('countdown',count_down)
dispatcher.add_handler(countdown_handler)

reply_handler = MessageHandler(Filters.text & (~Filters.command),reply)
dispatcher.add_handler(reply_handler)

j = updater.job_queue
job_daily = j.run_daily(good_night,days=(0, 1, 2, 3, 4, 5, 6),time=datetime.time(hour=2, minute=00,second=00,tzinfo=pytz.timezone('Asia/Seoul')))
#j.run_once(good_night,10)

updater.start_polling()
updater.idle()
