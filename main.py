from handlers import start_command, menu_callback

# Daftarkan handler ke dispatcher
dispatcher.add_handler(start_command)
dispatcher.add_handler(menu_callback)
