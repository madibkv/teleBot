from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, CallbackContext
import logging
import random
import datetime,pytz


updater = Updater(token='5122698218:AAFWpy_RooKtfQkGDL2Jlw9tKM1dC9e2MQM', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

CURRENT_VERSION = 'modiBot v3.2'
GOOD_NIGHT_MSGS = ['Спокойной ночи', 'Спокойной ночи, лю тя', 'Спокойной бро, лю тя', 'Спокойной ночи бро, лублу тя','лубу тебя, спокойной ночи',
'Спокойной ночи бро', 'Спокойной бро, лю тебя', 'Спи крепко бро, лублу тебя','Спокойной ночи, лублу тя','Спокойной, лу тя бро']

SECRET_MSG = """Хоба!! Секретное сообщение!!
В этом сообщении я буду говорить что в тебе классного, приготовься выслушивать комплименты(да, это так называется, а не «лапша на уши»!). Начнем с того, что пожалуй только с тобой я могу болтать по несколько часов в день, причем каждый день. Люблю просто болтать с тобой обо всем и ни о чем, просто угарать и рофлить с тобой. И вообще ты на самом деле оч интересная и приятная.
С тобой мне всегда комфортно. Нет никаких переживаний или страхов, нет волнения, просто чувство близости, чувство что человек свой, чувство теплоты и уюта. И это действительно очень круто 😎. Вряд ли мне бы хватило смелости написать это для кого то другого, но с тобой все иначе.
Мне очень нравится в тебе твой целеустремленный, стойкий, сильный характер. Может ты сама про себя так и не считаешь, но ты большой молодец, и очень много уже достигла, и еще большего достигнешь в будущем. Не смей никогда в себе сомневаться! 
А еще твоя доброта, то как ты ценишь своих друзей и близких, как всегда готова помочь. А еще то насколько ты умна и сообразительна это вообще отдельный разговор, единственная из моих друзей кто смог обыграть меня в шахматы 😂😂😂 (потом отыграюсь)
То шо ты всегда стремишься развиваться и учить что то новое, всегда двигаться, а не стоять на месте. 
Это я еще молчу про твою красоту, а то сообщение в телеге не вместится 😂
На самом деле это лишь малая часть из всех крутых вещей в тебе, бро, буду тебе о них переодически напоминать шоб не забывала. 
Лю тебя бро!
Спокойной ночи :)



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
	message = reply_hub(update.message.text)
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)
	#context.bot.send_message(chat_id=256346230,text=update.message.text)

def good_night(context : CallbackContext):
	message = random.choice(GOOD_NIGHT_MSGS)
	chance = random.randint(1,100)
	if chance == 7 or chance == 22 or chance == 85 or chance == 33 or chance == 77 or chance == 55 or chance == 25:
		message = SECRET_MSG

	debug_msg = message + '\n\nRandint: '+str(chance)

	context.bot.send_message(chat_id=256346230,text=debug_msg)
	context.bot.send_message(chat_id=724989540,text=message)

	
def count_down(update, context):
	delta = datetime.datetime(year=2022,month=6,day=17,hour=9,minute=45,tzinfo=pytz.timezone('Asia/Seoul')) - datetime.datetime.now(tz=pytz.timezone('Asia/Seoul'))
	seconds = delta.seconds

	days = delta.days
	hours = seconds//3600
	minutes = seconds%3600//60

	#lang = update_language(days,hours,minutes)

	message = 'Осталось: '+str(days)+'д '+ str(hours) + 'ч '+ str(minutes) + 'м'
	context.bot.send_message(chat_id=update.effective_chat.id,text=message)
	

def reply_hub(text):
	if text.split(' ')[0].lower() == 'добавь':
		add_to_list(text.split(' ')[1:])
		return 'Добавлено в список!'

	elif text.lower() == 'список':
		return "Список дел:\n" + read_list(text)
	
	elif text.split(' ')[0].lower() == 'удали':
		remove_from_list(text.split(' ')[1:])
		return 'Удалено из списка!'
	return '♥'


def add_to_list(text):
	f = open('todo_list.txt','a')
	for word in text:
		f.write(str(word)+" ")
	f.write('\n')
	f.close()

def read_list(text):
	try:
		f = open('todo_list.txt','r')
	except:
		return 'Список пуст'
	text = f.read()
	if not text:
		return 'Список пуст'
	return text


def remove_from_list(text):
	try:
		f = open('todo_list.txt','r')
	except:
		return 'Список пуст'
	lines = f.readlines()
	f.close()
	to_remove = ' '.join(text)+' '
	# print(to_remove+'1')
	# print(lines)
	f = open('todo_list.txt','w')
	for line in lines:
		#print(line.strip('\n')+'1')
		if line.strip('\n')!=to_remove:
			#print(line.strip('\n'))
			f.write(line)

	f.close()


# 724989540

start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

version_handler = CommandHandler('version',check_current_version)
dispatcher.add_handler(version_handler)

secret_handler = CommandHandler('aikosha',send_secret_message)
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
