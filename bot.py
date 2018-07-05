import telepot
from telepot.loop import MessageLoop

TOKEN = '583171379:AAGMemuXxpQB3u_KorK7xZ_uYokQ54k33SQ'
bot = telepot.Bot(TOKEN)

def handle(msg):
    """ Process request like '3+2' """
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"]
    try:
        answer = eval(text)
    except:
        answer = "Can't calculate :("
    bot.sendMessage(chat_id, "answer: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break
