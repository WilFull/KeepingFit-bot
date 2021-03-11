import telebot
import config  # Импорт config.py

bot = telebot.TeleBot(config.token)  # Передаём токен из файла config.py


# todo: Сделать вступительные слова с картинкой/стикером
@bot.message_handler(commands=['start'])
def welcome_start(message):
    sti = open('additional_files/sample_welcome_sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для спорта".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Чем я могу тебе помочь?')


@bot.message_handler(content_types=["text"])
def text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()  # запуск бота
