import telepot

from pprint import pprint

bot = telepot.Bot('583171379:AAGMemuXxpQB3u_KorK7xZ_uYokQ54k33SQ')

response = bot.getUpdates()

pprint(response)
