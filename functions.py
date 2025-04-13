from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def send_main_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("📦 Cari MOD", callback_data="menu_mod")],
        [InlineKeyboardButton("⭐ Premium", callback_data="menu_premium")],
        [InlineKeyboardButton("📊 Statistik", callback_data="menu_stats")],
        [InlineKeyboardButton("❓ Bantuan", callback_data="menu_help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "Selamat datang di ModFinderBot!\nSilakan pilih menu di bawah ini:"
    if update.message:
        update.message.reply_text(text, reply_markup=reply_markup)
    elif update.callback_query:
        update.callback_query.edit_message_text(text, reply_markup=reply_markup)

def handle_menu_callback(update, context):
    query = update.callback_query
    data = query.data

    if data == "menu_mod":
        query.answer()
        query.edit_message_text("Tulis nama game yang ingin kamu cari MOD-nya.")
    elif data == "menu_premium":
        query.answer()
        query.edit_message_text("Fitur Premium:\n- Tanpa shortlink\n- Akses lebih cepat\n\nUpgrade sekarang!")
    elif data == "menu_stats":
        query.answer()
        query.edit_message_text("Statistik sementara belum tersedia.")
    elif data == "menu_help":
        query.answer()
        query.edit_message_text("Butuh bantuan?\n\nKetik nama game untuk mencari MOD.\nHubungi admin: @adminmu")
