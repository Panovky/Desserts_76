import telepot

token = ''
my_id = 0
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")