import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the Telegram bot API token
bot = telegram.Bot('5668010305:AAEhbNX1fKG_9ySZlRJhxPtWEhe99s5tcMk')

# Define a function to handle the /start command
def start(update, context):
    bot.send_message(chat_id=update.message.chat_id, text="Welcome to the LinkMeUp bot! Please enter a phone number to get the WhatsApp chat link.")

# Define a function to handle incoming messages
def handle_message(update, context):
    message = update.message.text
    phone = message.strip()
    link = "https://api.whatsapp.com/send?phone="
    bot.send_message(chat_id=update.message.chat_id, text="Here is the link: " + link + phone)

# Set up a CommandHandler to listen for the /start command
start_handler = CommandHandler('start', start)

# Set up a MessageHandler to listen for incoming messages
message_handler = MessageHandler(Filters.text, handle_message)

# Set up an updater and dispatcher to handle incoming messages
updater = Updater('5668010305:AAEhbNX1fKG_9ySZlRJhxPtWEhe99s5tcMk')
dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)

# Start polling for incoming messages
updater.start_polling()
