from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, Updater
from handlers import start_command, handle_message, error
from config import token


if __name__ == '__main__':
    print('Starting bot')
    app = Application.builder().token(token).build()

    #COMMANDS
    app.add_handler(CommandHandler('start', start_command))

    #MESSAGES
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #ERRORS
    app.add_error_handler(error)

    #Polls the bot
    print('Polling')
    app.run_polling(poll_interval=3)

