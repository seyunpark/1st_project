import telegram

bot = telegram.Bot(token = '1391450532:AAH649LkqFFd-EsLfcVv8NOs0uxX8hXNBSA')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=1102663612, text="테스트입니다.")