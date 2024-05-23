from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import Update
from telegram.ext import CallbackContext

# Store user language preferences in a dictionary
user_languages = {}

def start(update: Update, context: CallbackContext):
    # Create an inline keyboard with language options
    keyboard = [
        [InlineKeyboardButton("ភាសាខ្មែរ 🇰🇭", callback_data='lang_km')],
        [InlineKeyboardButton("English 🇬🇧", callback_data='lang_en')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with language options
    update.message.reply_text("សូមជ្រើសរើសភាសា: \nPlease choose your language:", reply_markup=reply_markup)

def language_handler():
    return CommandHandler('start', start)

# Callback function to handle language selection
def set_language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    # Set user language based on their selection
    user_id = query.from_user.id
    if query.data == 'lang_en':
        user_languages[user_id] = 'en'
        query.edit_message_text(text="Language set to English 🇬🇧")
    elif query.data == 'lang_km':
        user_languages[user_id] = 'km'
        query.edit_message_text(text="Language set to Khmer 🇰🇭")

def language_button_handler():
    return CallbackQueryHandler(set_language, pattern='^lang_')

