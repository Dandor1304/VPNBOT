import telebot
import conf

bot = telebot.TeleBot(conf.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name} {message.from_user.last_name}!")
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Если у вас возникли проблемы обратитесь на почту: vpnsupport@gmail.com")

@bot.message_handler(commands=['ping'])
def ping(message):
    bot.send_message(message.chat.id, "Бот работает!")

@bot.message_handler(commands=['instruction'])
def main(message):
    file = open('./files/Otchet_lab_1.pdf', "rb")
    bot.send_document(message.chat.id, file)

bot.polling(none_stop=True)
