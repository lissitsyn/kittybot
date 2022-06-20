from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


TOKEN = '5559558579:AAGv_JJlTdccoGMPICEbCuZE0Kn0yibL-rQ'
CHAT_ID = 209017966

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['Который час?', 'Определи мой ip'],
                ['/random_digit']
            ])
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что вы включили меня, {}!'.format(name),
        reply_markup=buttons  
        )

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Привет, я KittyBot!')

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling(poll_interval=1.0)
updater.idle() 

#bot.send_message(chat_id, text) 