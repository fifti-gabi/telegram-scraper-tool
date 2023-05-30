import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = "5844613624:AAGu4zhheu2nFaYtKs1E8nI0oyFOCZVR_w0"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Vitajte! Napíšte /sendall <správa> na odoslanie hromadnej správy.")

def send_all(update, context):
    message = " ".join(context.args)
    for member in context.bot.get_chat_members(update.effective_chat.id):
        if member.user.is_bot:
            continue
        context.bot.send_message(chat_id=member.user.id, text=message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    send_all_handler = CommandHandler('sendall', send_all)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(send_all_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
