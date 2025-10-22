from telebot import TeleBot
from telebot import types 
from config import *

bot = TeleBot(token)


b1 = types.InlineKeyboardButton(f"{date_of_fortune} FORTUNE", callback_data="welcome_click_b1")
types = types.InlineKeyboardMarkup(row_width=1)
types.add(b1)

@bot.message_handler(commands=['start'])
def welcome_to_user(message):
    global welcome_m
    welcome_m = bot.send_message(message.chat.id, f"for FORTUNE of {date_of_fortune}, click on the button, you can also send /help command;", reply_markup=types)

@bot.callback_query_handler(func=lambda call: call.data == "welcome_click_b1")
def click_welcome_b1(call):
    bot.delete_message(call.id, welcome_m)
    bot.send_message(call.id, f"""
here you are; the fortune of the {date_of_fortune}
{fortune_of_the_date}
use /start to back""")

@bot.message_handler(commands=['set_time'])
def admin_set_time(message):
    user_id = message.from_user.id
    if user_id in admin:
        global frist_m
        frist_m = bot.send_message(f"{date_of_fortune} is for now, please send new time: \b for cancel send'cancel'")
        bot.register_next_step_handler(frist_m, admin_set_time1, cancel_done, set_m)

def admin_set_time1(message):
    if message.text == "cancel":
        global cancel_done
        cancel_done = bot.send_message(message.chat.id, "cancled.")
    else:
        global set_m
        set_m = bot.send_message(message.chat.id, "seted.")
            date_of_fortune = frist_m


@bot.message_handler(commands=['set_fortune'])
def admin_set_fourtune(message):
    user_id = message.from_user.id
    if user_id in admin:
        global frist_m1
        frist_m1 = bot.send_message(f"{fortune_of_the_date} is for now, please send new fortune: \b for cancel send'cancel'")
        bot.register_next_step_handler(frist_m1, admin_set_time1, cancel_done1, set_m1)

def admin_set_time1(message):
    if message.text == "cancel":
        global cancel_done1
        cancel_done1 = bot.send_message(message.chat.id, "cancled.")
    else:
        global set_m1
        set_m1 = bot.send_message(message.chat.id, "seted.")
            fortune_of_the_date = frist_m
            bot.send_message(chanel, f"new fortune for date {date_of_fortune}: \b {fortune_of_the_date} /br bot: {bot_id} chanel:{chanel}")    

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, """help:
use /start - for see fortune
admins:
use /set_time - for set time of the fortune
use /set_fortune - for set fortune of the date""")





bot.infinity.pooling()