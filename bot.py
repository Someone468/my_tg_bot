from botlogic import gen_pass
from botcoin import coin_flip
import random
import time, threading, schedule
import telebot

bot = telebot.TeleBot('7662970988:AAGMJWG12AImQCRC8_IKDZ5Ai-UEg7_-Iwc')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
        
@bot.message_handler(commands=['gen_pass'])
def send_gen_pass(message):
    password = gen_pass(10)
    bot.reply_to(message, f"Ваш пароль: {password}")

@bot.message_handler(commands=['coin_flip'])
def send_coin_flip(message):
    coin = coin_flip()
    bot.reply_to(message, f"Вам выпало: {coin}")

def beep(chat_id):
    bot.send_message(chat_id, text='Бип!')

@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(str(message.chat.id))
        bot.reply_to(message, f"Таймер установлен на каждые {sec} секунд!")
    else:
        bot.reply_to(message, 'Неправильный формат. Используйте: /set <секунды>')

@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(str(message.chat.id))
    bot.reply_to(message, "Таймер отключен!")

def schedule_runner():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=schedule_runner, daemon=True).start()

@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.reply_to(message, '/hello - Поздороваться\n/bye - Попрощаться\n/gen_pass - Сгенерировать безопасный пароль\n/coin_flip - Подкинуть монетку\n/set <секунды> - Поставить таймер\n/mem - Получить мем про программирование(у каждого разный шанс выпасть!)\n/watermelon - Арбуз')

@bot.message_handler(commands=['mem'])
def send_mem(message):
    meme_chance = random.randint(1,10)
    if meme_chance <= 5:
        with open(f'images\meme{1}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Мем обычной редкости!")
    elif meme_chance > 5 and meme_chance <= 8:
        with open(f'images\meme{2}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Мем необычной редкости!")
    elif meme_chance > 8 and meme_chance <= 10:
        with open(f'images\meme{3}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Мем большой редкости!")

@bot.message_handler(commands=['watermelon'])
def send_mem(message):
    watermelon_chance = random.randint(1,11)
    if watermelon_chance <= 5:
        with open(f'images\watermelon{1}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Арбуз обычной редкости!")
    elif watermelon_chance > 5 and watermelon_chance <= 8:
        with open(f'images\watermelon{2}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Арбуз необычной редкости!")
    elif watermelon_chance > 8 and watermelon_chance <= 10:
        with open(f'images\watermelon{3}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Арбуз большой редкости!")
    elif watermelon_chance > 10 and watermelon_chance <= 11:
        with open(f'images\watermelon{4}.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
            bot.reply_to(message, "Секретный арбуз!")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
