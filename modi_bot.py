from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackContext
import logging
import random
import datetime,pytz


updater = Updater(token='5122698218:AAFWpy_RooKtfQkGDL2Jlw9tKM1dC9e2MQM', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

GOOD_NIGHT_MSGS = ['Спокойной ночи', 'Спокойной ночи, лю тя', 'Спокойной бро, лю тя', 'Спокойной ночи бро, лублу тя','лубу тебя, спокойной ночи',
'Спокойной ночи бро', 'Спокойной бро, лю тебя', 'Спи крепко бро, лублу тебя','Спокойной ночи, лублу тя','Спокойной, лу тя бро']


def start(update, context):
	message = 'Халооооу'
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)
	user_id = update.message.from_user.id
	print(user_id)


def reply(update,context):
	message = '♥'
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)

def good_night(context : CallbackContext):
	message = random.choice(GOOD_NIGHT_MSGS)
	#context.bot.send_message(chat_id=256346230,text=message)
	context.bot.send_message(chat_id=724989540,text=message)



# 724989540

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

reply_handler = MessageHandler(Filters.text & (~Filters.command),reply)
dispatcher.add_handler(reply_handler)

j = updater.job_queue
job_daily = j.run_daily(good_night,days=(0, 1, 2, 3, 4, 5, 6),time=datetime.time(hour=2, minute=00,second=00,tzinfo=pytz.timezone('Asia/Seoul')))
#j.run_once(good_night,10)

updater.start_polling()
