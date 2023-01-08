import telepot

token = '5892884887:AAGLooZZxTHYXhQLkYa1fFAc-frQfg04u00'
my_id = 303659314
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")