import telepot

token = '5828808995:AAGloZrhyiPqRyl8kDU5epZ9NmatygI7Sew'
my_id = 303659314
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(my_id, text, parse_mode="Markdown")