from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from functions import send_main_menu, handle_menu_callback

# Handler untuk perintah /start
def start_handler(update: Update, context: CallbackContext):
    send_main_menu(update, context)

# Handler untuk callback tombol menu
def callback_query_handler(update: Update, context: CallbackContext):
    handle_menu_callback(update, context)

# Daftarkan handler
start_command = CommandHandler("start", start_handler)
menu_callback = CallbackQueryHandler(callback_query_handler, pattern="^menu_")
