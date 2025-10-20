from telegram import Update
from telegram.ext import ContextTypes
from weather import get_weather
from config import BOT_USERNAME

#COMMANDS
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I'm a Weather Bot. I can help you check the weather! 🌦 To check the weather, please type the name of your city.")


#RESPONSES
async def handle_response(text: str) -> str:
    city = text.strip()
    if not city:
        return "🌤️ Ask me"
    return await get_weather(city)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in  {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = await handle_response(new_text)
        else:
            return
    else:
        response: str = await handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')