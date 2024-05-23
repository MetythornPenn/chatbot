from telegram.ext import CommandHandler
from handlers.language import user_languages


def deposit_info(update, context):
    user_id = update.message.from_user.id
    language = user_languages.get(user_id, 'en')

    if language == 'km':
        response = (
            "សេវាកម្មបញ្ញើ:\n"
            "គណនីសន្សំធនាគារ\n"
            "អត្រាការប្រាក់: 1% ទៅ 3% ក្នុងមួយឆ្នាំ\n"
            "រូបិយប័ណ្ណ: KHR & USD\n"
            "ការបង់ប្រាក់: ចុងខែ ឬ បន្សំ"
        )
    else:
        response = (
            "Deposit Services:\n"
            "Bank Savings Account\n"
            "Interest Rate: 1% to 3% per annum\n"
            "Currency: KHR & USD\n"
            "Payment: Monthly or Accumulative"
        )

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def deposit_info_handler():
    return CommandHandler('deposit_info', deposit_info)


def deposit(update, context):
    user_id = update.message.from_user.id
    language = user_languages.get(user_id, 'en')

    amount = context.args[0] if context.args else None

    if amount:
        if language == 'km':
            deposit_info = f"បានដាក់ប្រាក់ចំនួន ${amount}."
        else:
            deposit_info = f"Successfully deposited ${amount}."
    else:
        if language == 'km':
            deposit_info = "សូមផ្តល់ចំនួនដាក់ប្រាក់។"
        else:
            deposit_info = "Please provide an amount to deposit."

    context.bot.send_message(chat_id=update.effective_chat.id, text=deposit_info)


def deposit_handler():
    return CommandHandler('deposit', deposit)
