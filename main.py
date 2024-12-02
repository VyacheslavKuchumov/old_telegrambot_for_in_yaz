import telebot
from telebot import types
from datetime import datetime


BOT_TOKEN=""


print("starting up....")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):

    print("\n***User activity detected!***\n" + call.data)
    print(call.from_user.first_name)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)

    print()
    chat_id = call.message.chat.id
    if call.data == "block1":
        bot.send_message(chat_id, "В разработке...")
    if call.data == "block2":
        bot.send_message(chat_id, "В разработке...")

    if call.data == "block4":
        button_studClub = types.InlineKeyboardButton('Студклуб', callback_data='studClub')
        button_coworking = types.InlineKeyboardButton('Коворкинг', callback_data='coworking')
        button_fok = types.InlineKeyboardButton('Фок', callback_data='fok')
        button_actovi = types.InlineKeyboardButton('Актовый зал', callback_data='actovi')
        button_sport3 = types.InlineKeyboardButton('Спортзал №3', callback_data='sport3')
        button_bufet4k = types.InlineKeyboardButton('Буфет', callback_data='bufet4k')
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(button_studClub)
        keyboard.add(button_coworking)
        keyboard.add(button_fok)
        keyboard.add(button_actovi)
        keyboard.add(button_sport3)
        keyboard.add(button_bufet4k)
        bot.send_message(chat_id, text='Куда идем?', reply_markup=keyboard)

    if call.data == "studClub":
        bot.send_message(chat_id, "Заходим в 4 корпус, проходим пост охраны и поворачиваем направо. Проходим мимо гардероба и ищем кабинет А118 с надписью «Студклуб» и о, мы на месте!")
        with open("img/studClub.jpg", "rb") as img:
            bot.send_photo(chat_id, img)
            img.close()

    if call.data == "coworking":
        bot.send_message(chat_id, "Заходим в 4 корпус, проходим пост охраны и поворачиваем налево. Идем по коридору прямо до стеклянной двери и спускаемся вниз по лестнице. Открываем дверь, поворачиваем направо, и мы на месте!")
        with open("img/CowWorking.jpg", "rb") as img:
            bot.send_photo(chat_id, img)
            img.close()
    if call.data == "fok":
        bot.send_message(chat_id, "Заходим в 4 корпус, проходим пост охраны и спускаемся вниз по лестнице. Под лестницей увидите дверь, снова спускаетесь вниз по лестнице, и вы на месте!")
        with open("img/fuc.jpg", "rb") as img:
            bot.send_photo(chat_id, img)
            img.close()
    if call.data == "actovi":
        bot.send_message(chat_id, "Заходим в 4 корпус, проходим пост охраны и поворачиваем направо. Проходим прямо по коридору до конца до холла перед дверьми актового зала, и мы на месте!")
        with open("img/actovi.jpg", "rb") as img:
            bot.send_photo(chat_id, img)
            img.close()
    if call.data == "sport3":
        bot.send_message(chat_id, "Заходим в 4 корпус, проходим пост охраны и спускаемся вниз по лестнице. Идем прямо по коридору до конца, поворачиваем направо и снова прямо до конца по коридору. Видим железную дверь с надписью спортзал, заходим, и мы пришли!")
        with open("img/sportik.jpg", "rb") as img:
            bot.send_photo(chat_id, img)
            img.close()
    if call.data == "bufet4k":
        bot.send_message(chat_id,"Заходим в 4 корпус, проходим пост охраны и поворачиваем направо. Проходим мимо гардероба до кабинета справа с надписью буфет, и мы на месте!")
        with open("img/bufet.jpg", "rb") as img:
            bot.send_photo(chat_id, img)
            img.close()
    if call.data == "block5":
        bot.send_message(chat_id, "В разработке...")





@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("\n***Start command detected!***")
    print(message.from_user.first_name)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    bot.reply_to(message, "Привет! Я лидер факультета иностранных языков,  помогу тебе ориентироваться в нашем университете")
    # img = open("img/goofy-cat.png", "rb")
    # bot.send_photo(message.chat.id, img)

    chat_id = message.chat.id


    button_1k = types.InlineKeyboardButton('1 корпус', callback_data='block1')
    button_2k = types.InlineKeyboardButton('2 корпус', callback_data='block2')
    button_4k = types.InlineKeyboardButton('4 корпус', callback_data='block4')
    button_5k = types.InlineKeyboardButton('5 корпус', callback_data='block5')

    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button_1k)
    keyboard.add(button_2k)
    keyboard.add(button_4k)
    keyboard.add(button_5k)

    bot.send_message(chat_id, text='О каком корпусе хочешь узнать?', reply_markup=keyboard)




@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Чтобы перезапустить бота пропишите команду /start")



# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     msg_id = message.chat.id
#     print("New message incoming!")
#     print("User said: "+message.text+"\n")
#     msg =  message.text.lower()
#     if msg == "где находится коворкинг?" or msg == "где находится коворкинг":
#         answer = "Заходим в 4 корпус, проходим пост охраны и поворачиваем налево. Идем по коридору прямо до стеклянной двери и спускаемся вниз по лестнице. Открываем дверь, поворачиваем направо, и мы на месте!"
#         bot.reply_to(message, answer)
#         with open("img/CowWorking.jpg", "rb") as img:
#             bot.send_photo(msg_id, img)
#             img.close()
#
#
#     elif msg == "где находится студклуб?" or msg == "где находится студклуб":
#         answer = "Заходим в 4 корпус, проходим пост охраны и поворачиваем направо. Проходим мимо гардероба и ищем кабинет А118 с надписью «Студклуб» и о, мы на месте!"
#         bot.reply_to(message, answer)
#         with open("img/studClub.jpg", "rb") as img:
#             bot.send_photo(msg_id, img)
#             img.close()
#     else:
#         answer = "Не понял( Попробуйте еще раз"
#         bot.reply_to(message, answer)
#




bot.infinity_polling()

