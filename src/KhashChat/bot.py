from telegram.ext import Updater
from config import TELEGRAM_TOKEN
from handlers import start, help, saving, deposit, loan  # Adjust as needed for your handlers

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(start.start_handler())
    dispatcher.add_handler(help.help_callback_handler())
    dispatcher.add_handler(saving.saving_handler())
    dispatcher.add_handler(saving.q1_handler())
    dispatcher.add_handler(saving.q2_handler())
    dispatcher.add_handler(saving.q3_handler())
    dispatcher.add_handler(saving.q4_handler())
    dispatcher.add_handler(saving.q5_handler())
    dispatcher.add_handler(saving.main_menu_handler())
    dispatcher.add_handler(saving.get_conversation_handler())
    dispatcher.add_handler(deposit.deposit_handler())
    dispatcher.add_handler(deposit.deposit_info_handler())
    dispatcher.add_handler(loan.loan_info_handler())
    dispatcher.add_handler(start.language_button_handler())

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
