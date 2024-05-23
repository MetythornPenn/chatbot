from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Savings account details
CURRENT_SAVINGS_USD = None
INTEREST_RATE = 2

SET_SAVINGS = range(1)
def saving(update, context):
    keyboard = [
        [InlineKeyboardButton("What is my current savings?", callback_data='q1')],
        [InlineKeyboardButton("What is the interest rate?", callback_data='q2')],
        [InlineKeyboardButton("What is the last transaction?", callback_data='q3')],
        [InlineKeyboardButton("How much can I withdraw?", callback_data='q4')],
        [InlineKeyboardButton("How do I deposit money?", callback_data='q5')],
        [InlineKeyboardButton("Set my current savings", callback_data='set_savings')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Savings Q&A", reply_markup=reply_markup)

def q1(update, context):
    query = update.callback_query
    query.answer()

    if CURRENT_SAVINGS_USD is None:
        reply_text = "You haven't set your current savings yet. Please use the 'Set my current savings' option to update it."
    else:
        reply_text = f"Your current savings is ${CURRENT_SAVINGS_USD}."
    keyboard = [
        [InlineKeyboardButton("Back to main menu", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=reply_text, reply_markup=reply_markup)

def q2(update, context):
    query = update.callback_query
    query.answer()

    reply_text = f"The interest rate on your savings account is {INTEREST_RATE}%."
    keyboard = [
        [InlineKeyboardButton("Back to main menu", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=reply_text, reply_markup=reply_markup)

def q3(update, context):
    query = update.callback_query
    query.answer()

    reply_text = "Your last transaction was a deposit of $500 on 2024-05-15."
    keyboard = [
        [InlineKeyboardButton("Back to main menu", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=reply_text, reply_markup=reply_markup)

def q4(update, context):
    query = update.callback_query
    query.answer()

    if CURRENT_SAVINGS_USD is None:
        reply_text = "You haven't set your current savings yet. Please use the 'Set my current savings' option to update it."
    else:
        reply_text = f"You can withdraw up to ${CURRENT_SAVINGS_USD} from your savings account."
    keyboard = [
        [InlineKeyboardButton("Back to main menu", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=reply_text, reply_markup=reply_markup)

def q5(update, context):
    query = update.callback_query
    query.answer()

    reply_text = "To deposit money into your savings account, you can visit your nearest FTB branch or use our online banking platform."
    keyboard = [
        [InlineKeyboardButton("Back to main menu", callback_data='main_menu')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text=reply_text, reply_markup=reply_markup)

def set_savings(update, context):
    query = update.callback_query
    query.answer()

    context.user_data['set_savings'] = True
    query.message.reply_text("Please enter your current savings amount in US Dollars:")

    return SET_SAVINGS

def set_savings_amount(update, context):
    global CURRENT_SAVINGS_USD
    try:
        savings_amount = float(update.message.text)
        CURRENT_SAVINGS_USD = savings_amount
        update.message.reply_text(f"Your current savings has been set to ${CURRENT_SAVINGS_USD}.")
    except ValueError:
        update.message.reply_text("Invalid amount. Please enter a number.")
        return SET_SAVINGS

    main_menu(update, context)
    return ConversationHandler.END

def main_menu(update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("What is my current savings?", callback_data='q1')],
        [InlineKeyboardButton("What is the interest rate?", callback_data='q2')],
        [InlineKeyboardButton("What is the last transaction?", callback_data='q3')],
        [InlineKeyboardButton("How much can I withdraw?", callback_data='q4')],
        [InlineKeyboardButton("How do I deposit money?", callback_data='q5')],
        [InlineKeyboardButton("Set my current savings", callback_data='set_savings')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text="Savings Q&A", reply_markup=reply_markup)

def saving_handler():
    return CommandHandler('saving', saving)

def q1_handler():
    return CallbackQueryHandler(q1, pattern='^q1$')

def q2_handler():
    return CallbackQueryHandler(q2, pattern='^q2$')

def q3_handler():
    return CallbackQueryHandler(q3, pattern='^q3$')

def q4_handler():
    return CallbackQueryHandler(q4, pattern='^q4$')

def q5_handler():
    return CallbackQueryHandler(q5, pattern='^q5$')

def set_savings_handler():
    return CallbackQueryHandler(set_savings, pattern='^set_savings$')

def set_savings_amount_handler():
    return MessageHandler(Filters.text & ~Filters.command, set_savings_amount)

def main_menu_handler():
    return CallbackQueryHandler(main_menu, pattern='^main_menu$')

def get_conversation_handler():
    return ConversationHandler(
        entry_points=[set_savings_handler()],
        states={
            SET_SAVINGS: [set_savings_amount_handler()]
        },
        fallbacks=[main_menu_handler()]
    )