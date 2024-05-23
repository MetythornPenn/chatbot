from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext
from handlers.language import user_languages

def start(update: Update, context: CallbackContext):
    # Create an inline keyboard with language options
    keyboard = [
        [InlineKeyboardButton("ភាសាខ្មែរ 🇰🇭", callback_data='lang_km')],
        [InlineKeyboardButton("English 🇬🇧", callback_data='lang_en')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with language options
    update.message.reply_text("សូមជ្រើសរើសភាសា: \nPlease choose your language:", reply_markup=reply_markup)

def set_language(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    # Set user language based on their selection
    user_id = query.from_user.id
    if query.data == 'lang_en':
        user_languages[user_id] = 'en'
        query.edit_message_text(text="Language set to English 🇬🇧\n")
    elif query.data == 'lang_km':
        user_languages[user_id] = 'km'
        query.edit_message_text(text="ភាសាត្រូវបានកំណត់ជាភាសាខ្មែរ 🇰🇭\n")

    # After setting language, show the help menu
    show_help_menu(update, context)

def show_help_menu(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    language = user_languages.get(user_id, 'en')

    if language == 'km':
        text = "ជ្រើសរើសជំនួយដែលអ្នកចង់បាន:"
        button_texts = ["សន្សំ", "ដាក់ប្រាក់", "ឥណទាន"]
    else:
        text = "Choose the help you need:"
        button_texts = ["Saving", "Deposit", "Loan"]

    keyboard = [
        [InlineKeyboardButton(button_texts[0], callback_data='help_saving')],
        [InlineKeyboardButton(button_texts[1], callback_data='help_deposit')],
        [InlineKeyboardButton(button_texts[2], callback_data='help_loan')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=reply_markup)

def start_handler():
    return CommandHandler('start', start)

def language_button_handler():
    return CallbackQueryHandler(set_language, pattern='^lang_')
