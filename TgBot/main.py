import telebot
from telebot import types 

api  = '7890702832:AAENWFsNVllpZ5jELn1dLzeZS9nLJu0W-5E'
bot = telebot.TeleBot(api)


user_coins = {}

@bot.message_handler(commands=['start'])
def user_phone(message):
    user_coins[message.chat.id] = 0  
    bot.send_message(message.chat.id, f'Xush kelibsiz {message.from_user.first_name}')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    contact_btn = types.KeyboardButton(text="Contact yuborish", request_contact=True)
    markup.add(contact_btn)
    bot.send_message(message.chat.id, f'Iltimos, contact yuboring:', reply_markup=markup)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    contact = message.contact.phone_number
    bot.send_message(message.chat.id, f"Rahmat! Sizning telefon raqamingiz: {contact}")
    
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1  =  types.KeyboardButton('Koin qoshish ➕')
    btn2  =  types.KeyboardButton('Koin ayirish ➖')
    btn3  =  types.KeyboardButton('Koinlarni ko\'rish 👀')
    markup.add(btn1, btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id, 'Davom eting:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Koin qoshish ➕')
def add_coin(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    add_coin_button_1  =  types.KeyboardButton('➕ 1 coin qoshish')
    add_coin_button_2  =  types.KeyboardButton('➕ 2 coin qoshish')
    add_coin_button_3  =  types.KeyboardButton('➕ 5 coin qoshish')
    add_coin_button_4  =  types.KeyboardButton('➕ 10 coin qoshish')
    markup.add(add_coin_button_1, add_coin_button_2)
    markup.add(add_coin_button_3, add_coin_button_4)
    bot.send_message(message.chat.id, "Coin qo'shish turlaridan qaysi biri qulay?\nO'zingizga qulay turini tanlang!", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith('➕'))
def increment_coins(message):
    coin_value = int(message.text.split(' ')[1])  
    user_coins[message.chat.id] += coin_value 
    bot.send_message(message.chat.id, f"{coin_value} coin qo'shildi!\nHozirgi coinlar soni: {user_coins[message.chat.id]}")
    

    go_back_to_main_menu(message)

@bot.message_handler(func=lambda message: message.text == 'Koin ayirish ➖')
def subtraction_coin(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    subtraction_coin_button_1  =  types.KeyboardButton('➖ 2 coin ayirish')
    markup.add(subtraction_coin_button_1)
    bot.send_message(message.chat.id, 'Necha koin ayirmoqchisiz?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith('➖'))
def decrement_coins(message):
    coin_value = int(message.text.split(' ')[1])  
    user_coins[message.chat.id] -= coin_value  
    if user_coins[message.chat.id] < 0:
        user_coins[message.chat.id] = 0  
    bot.send_message(message.chat.id, f"{coin_value} coin ayirildi!\nHozirgi coinlar soni: {user_coins[message.chat.id]}")


    go_back_to_main_menu(message)


@bot.message_handler(func=lambda message: message.text == 'Koinlarni ko\'rish 👀')
def show_coins(message):
    current_coins = user_coins.get(message.chat.id, 0)
    bot.send_message(message.chat.id, f"Sizning hozirgi coinlaringiz soni: {current_coins}")


def go_back_to_main_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1  =  types.KeyboardButton('Koin qoshish ➕')
    btn2  =  types.KeyboardButton('Koin ayirish ➖')
    btn3  =  types.KeyboardButton('Koinlarni ko\'rish 👀')
    markup.add(btn1, btn2)
    markup.add(btn3)
    bot.send_message(message.chat.id, 'Davom eting:', reply_markup=markup)

bot.polling()
