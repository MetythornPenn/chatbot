from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackQueryHandler, CallbackContext
from handlers.language import user_languages

def help_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id

    # Check if the user has selected their language
    if user_id not in user_languages:
        query.edit_message_text(text="Please choose your language first.")
        return

    language = user_languages[user_id]

    if query.data == 'help_saving':
        if language == 'km':
            text = "ព័ត៌មានអំពីការសន្សំ:\n\n"
            text += "/saving - ពិនិត្យសមតុល្យសន្សំ"
        else:
            text = "Information about Saving:\n\n"
            text += "/saving - Check your savings balance"
    elif query.data == 'help_deposit':
        if language == 'km':
            text = "ព័ត៌មានអំពីការដាក់ប្រាក់:\n\n"
            text += "/deposit_info - ព័ត៌មានអំពីការដាក់ប្រាក់\n"
            text += "/deposit [amount] - ដាក់ប្រាក់"
        else:
            text = "Information about Deposit:\n\n"
            text += "/deposit_info - Information about deposits\n"
            text += "/deposit [amount] - Deposit funds"
    elif query.data == 'help_loan':
        if language == 'km':
            text = "ព័ត៌មានអំពីឥណទាន:\n\n"
            text += "/loan_info - ព័ត៌មានអំពីឥណទាន"
        else:
            text = "Information about Loans:\n\n"
            text += "/loan_info - Information about loans"

    query.edit_message_text(text=text)

def help_callback_handler():
    return CallbackQueryHandler(help_callback, pattern='^help_')
