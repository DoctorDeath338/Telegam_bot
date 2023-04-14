import telebot
from telebot import types
import random
token="6149359269:AAG6wpw8YvV2PtfZu5aEDOmy1GWwJ4Bhtwo"
bot=telebot.TeleBot(token)
hp=dmg=0
dict_rase={"Эльф":{"hp":110,"dmg":70}, 
           "Маг":{"hp":135, "dmg":160},
           "Орг":{"hp":145, "dmg":195}, 
           "Человек":{"hp":125, "dmg":125},
           "Гном": {"hp":85, "dmg":140}}
dict_prof={"Мечник":{"hp":30, "dmg":45},
           "Лучник":{"hp":20, "dmg":50},
           "Целитель":{"hp":55, "dmg":25}}
mnstr=["Зомби", "Вампир", "Инопланетяне", "Дракон", "Мутант"]
def rase_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for rase in dict_rase.keys():
        keyboard.add(types.KeyboardButton(text=rase))
    return keyboard
def prof_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for prof in dict_prof.keys():
        keyboard.add(types.KeyboardButton(text=prof))
    return keyboard 
def play_menu():
    keyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1= types.KeyboardButton("В путь")
    but2= types.KeyboardButton("Назад")
    keyboard.add(but1, but2)
    return keyboard
def create_mnstr():
    mnstr_name=random.choice(mnstr)
    mnstr_hp=random.randint(65,180)
    mnstr_dmg=random.randint(45, 160)
    return[mnstr_name, mnstr_hp, mnstr_dmg]
@bot.message_handler(commands=["start"])
def start(message):
    keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1= types.KeyboardButton("Играть")
    but2= types.KeyboardButton("Об игре (тоесть ничего интересного)")
    keyboard.add(but1, but2)
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в мой телеграмм бот! Тут ты можешь поиграть... ну и все в принципе))", reply_markup= keyboard)
def quest():
    keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
    but14= types.KeyboardButton("Начать")
    but13= types.KeyboardButton("Убежать")
    but8= types.KeyboardButton ("Назад")
    keyboard.add(but8, but13, but14)
    return keyboard
    # bot.send_message(message.chat.id, "У тебя есть новое приключение! Что ты хочешь сделать?", reply_markup= keyboard)
@bot.message_handler(content_types=['text'])
def answer(message):
    global hp, dmg
    victim= create_mnstr()
    if (message.text== "Об игре (тоесть ничего интересного)"):
        bot.send_message(message.chat.id, "Ну и нафиг ты сюда пришел? Ничё тут нет, дуй отсюда")
    if (message.text == "Играть"):
        keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        but3= types.KeyboardButton("Эльф")
        but4= types.KeyboardButton("Маг")
        but5= types.KeyboardButton("Гном")
        but6= types.KeyboardButton("Человек")
        but7= types.KeyboardButton("Орг")
        but8= types.KeyboardButton ("Назад")
        keyboard.add(but3, but4, but5, but6, but7, but8)
        bot.send_message(message.chat.id, "Выбери расу, за которую ты будешь играть", reply_markup= rase_menu())   
    if  (message.text == "Назад"):
        hp=dmg=0
        keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1= types.KeyboardButton("Играть")
        but2= types.KeyboardButton("Об игре (тоесть ничего интересного)")
        keyboard.add(but1, but2)
        bot.send_message(message.chat.id, "Привет! Добро пожаловать в мой телеграмм бот! Тут ты можешь поиграть... ну и все в принципе))", reply_markup= keyboard)
    if (message.text == "Эльф"):
        hp+=dict_rase["Эльф"]["hp"] 
        dmg+=dict_rase["Эльф"]["dmg"]
        # keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        # but9= types.KeyboardButton("Мечник")
        # but10= types.KeyboardButton("Лучник")
        # but11= types.KeyboardButton("Целитель")
        # but8= types.KeyboardButton ("Назад")
        # keyboard.add(but9, but10, but11, but8)
        bot.send_message(message.chat.id, f"Вы эльф, ваше здоровье={hp}, ваше урон={dmg}Выбери профессию", reply_markup= prof_menu())
        image= open ("5c23bd11167785f49e8ffeabe09d85d8.jpg", "rb")
        bot.send_photo(message.chat.id,image)
    if (message.text == "Маг"):
        hp+=dict_rase["Маг"]["hp"] 
        dmg+=dict_rase["Маг"]["dmg"]
        # keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        # but9= types.KeyboardButton("Мечник")
        # but10= types.KeyboardButton("Лучник")
        # but11= types.KeyboardButton("Целитель")
        # but8= types.KeyboardButton ("Назад")
        # keyboard.add(but9, but10, but11, but8)
        image= open ("9bfc65c1e13e68105d9e352371d88aaf.jpg", "rb")
        bot.send_photo(message.chat.id,image)
        bot.send_message(message.chat.id, "Выбери профессию", reply_markup= prof_menu())
    if (message.text == "Орг"):
        hp+=dict_rase["Орг"]["hp"] 
        dmg+=dict_rase["Орг"]["dmg"]
        # keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        # but9= types.KeyboardButton("Мечник")
        # but10= types.KeyboardButton("Лучник")
        # but11= types.KeyboardButton("Целитель")
        # but8= types.KeyboardButton ("Назад")
        # keyboard.add(but9, but10, but11, but8)
        image= open ("d3968af917617d794b1502b43d155036.jpg", "rb")
        bot.send_photo(message.chat.id,image)
        bot.send_message(message.chat.id, "Выбери профессию", reply_markup= prof_menu())
    if (message.text == "Гном"):
        hp+=dict_rase["Гном"]["hp"] 
        dmg+=dict_rase["Гном"]["dmg"]
        # keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        # but9= types.KeyboardButton("Мечник")
        # but10= types.KeyboardButton("Лучник")
        # but11= types.KeyboardButton("Целитель")
        # but8= types.KeyboardButton ("Назад")
        # keyboard.add(but9, but10, but11, but8)
        image= open ("rishikesh-nandlaskar-mushroomgoblin-comp02.jpg", "rb")
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, "Выбери профессию", reply_markup= prof_menu())
    if (message.text == "Человек"):
        hp+=dict_rase["Человек"]["hp"] 
        dmg+=dict_rase["Человек"]["dmg"]
        # keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        # but9= types.KeyboardButton("Мечник")
        # but10= types.KeyboardButton("Лучник")
        # but11= types.KeyboardButton("Целитель")
        # but8= types.KeyboardButton ("Назад")
        # keyboard.add(but9, but10, but11, but8)
        image= open("1625657003_1-phonoteka-org-p-sila-dukha-art-krasivo-1.jpg", "rb")
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, "Выбери профессию", reply_markup= prof_menu())
    if (message.text == "Мечник"):
        hp+=dict_prof["Мечник"]["hp"]
        dmg+=dict_prof["Мечник"]["dmg"]
        image= open("viking-sword-and-scabbard-mechi-oruzhie-runy-stal.jpg", "rb")
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, "Вы хотите отправится в путь?", reply_markup= quest())
    if (message.text == "Лучник"):
        hp+=dict_prof["Лучник"]["hp"]
        dmg+=dict_prof["Лучник"]["dmg"]
        image= open("viking-sword-and-scabbard-mechi-oruzhie-runy-stal.jpg", "rb")
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, "Вы хотите отправится в путь?", reply_markup= quest())
    if (message.text == "Целитель"):
        hp+=dict_prof["Целитель"]["hp"]
        dmg+=dict_prof["Целитель"]["dmg"]
        image= open("1646092095_6-chakiris-club-p-tselitel-fentezi-fentezi-oboi-8.jpg", "rb")
        bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, "Вы хотите отправится в путь?", reply_markup= quest())
    if (message.text == "Начать"):
        event= random.randint(1, 2)
        if event == 1:
            keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
            but14= types.KeyboardButton("Начать")
            but13= types.KeyboardButton("Убежать")
            but8= types.KeyboardButton ("Назад")
            keyboard.add(but8, but13, but14)
            bot.send_message(message.chat.id, "Тут никого...", reply_markup= keyboard)
        if event == 2:
            keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
            but15= types.KeyboardButton("Атака")
            but16= types.KeyboardButton("Сбежать")
            keyboard.add(but15, but16)
            bot.send_message(message.chat.id, f"Вы встретили врага! Его зовут{victim[0]}, у него здоровья {victim[1]}, а его урон {victim[2]}. Сделай выбор...", reply_markup= keyboard)
    if (message.text == "Атака"):
        victim[1]-=dmg
        if victim[1]<=0:
            hp+=10
            dmg+=5
            bot.send_message(message.chat.id, f"Ты победил врага! Твое здоровье={hp}, а твой урон равен{dmg}", reply_markup= quest())
        elif victim[1]>0:
            hp-=victim[2]
            bot.send_message(message.chat.id, f"Твое здоровье={hp}, здоровье врага={victim[1]}. Твой урон={dmg}, урон врага={victim[2]}")
            if hp<=0:
                keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
                but17= types.KeyboardButton("Назад в меню")
                keyboard.add(but17)
                bot.send_message(message.chat.id, "Ты проиграл", reply_markup=keyboard)
            if hp>0:
                keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
                but15= types.KeyboardButton("Атака")
                but16= types.KeyboardButton("Сбежать")
                keyboard.add(but15, but16)
                bot.send_message(message.chat.id, "Хотите аткаковать снова?", reply_markup=keyboard)         
    if message.text =="Сбежать":
        run= random.randint(1,2)
        if run == 1:
            bot.send_message(message.chat.id, f"Вам удалось сбежать! Хотите продолжить?", reply_markup=quest())  
        if run == 2:
            hp-=victim[2]
            bot.send_message(message.chat.id, f"Вам не удалось сбежать")    
            if hp<=0:
                keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
                but17= types.KeyboardButton("Назад в меню")
                keyboard.add(but17)
                bot.send_message(message.chat.id, f"Вы проиграли", reply_markup=keyboard)
            if hp>0:
                keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
                but15= types.KeyboardButton("Атака")
                but16= types.KeyboardButton("Сбежать")
                keyboard.add(but15, but16)
                bot.send_message(message.chat.id, f"Хотите атаковать снова? Ваше  здоровье= {hp}", reply_markup=keyboard)  
    if message.text == "Убежать":
        keyboard= types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1= types.KeyboardButton("Играть")
        but2= types.KeyboardButton("Об игре (тоесть ничего интересного)")
        keyboard.add(but1, but2)
        bot.send_message(message.chat.id, f"Вы сбежали! Что хотите сделать?")   
bot.polling(non_stop=True)
