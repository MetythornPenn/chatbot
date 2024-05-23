from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext

from handlers.language import user_languages

def loan_info_start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    # Check if the user has selected their language
    if user_id not in user_languages:
        update.message.reply_text("Please choose your language first.")
        return

    language = user_languages[user_id]

    if language == 'km':
        text = "សូមជ្រើសរើសអ្វីដែលអ្នកចង់ដឹងអំពីឥណទាន:"
        button_texts = ["ទូទៅ", "លក្ខណៈសម្បត្តិ", "ឯកសារត្រូវការ"]
    else:
        text = "Please choose what you want to know about the loan:"
        button_texts = ["Overview", "Eligibility", "Required Documents"]

    keyboard = [
        [InlineKeyboardButton(button_texts[0], callback_data='loan_overview')],
        [InlineKeyboardButton(button_texts[1], callback_data='loan_eligibility')],
        [InlineKeyboardButton(button_texts[2], callback_data='loan_documents')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text, reply_markup=reply_markup)

def loan_info_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id

    # Check if the user has selected their language
    if user_id not in user_languages:
        query.edit_message_text("Please choose your language first.")
        return

    language = user_languages[user_id]

    if query.data == 'loan_overview':
        if language == 'km':
            text = (
                "ទូទៅអំពីឥណទាន:\n"
                "- ទឹកប្រាក់កម្ចី: USD 500 – 20000 អាចដលះទៅ 06 ដងនៃប្រាក់ខែសុទ្ធ\n"
                "- រយៈពេលកម្ចី: ចំនួនខែរហូតដលះ 36\n"
                "- រូបិយប័ណ្ណ: KHR & USD\n"
                "- អត្រាការប្រាក់: រហូតដលះ 18% ក្នុងមួយឆ្នាំ\n"
                "- ជម្រើសនៃការបង់ប្រាក់:\n"
                "  1. គោលការណ៍និងការប្រាក់ថេរ\n"
                "  2. គោលការណ៍ថេរ + ការប្រាក់ថេរ\n"
                "- ថ្លៃដំណើរការ: 1% នៃចំនួនអនុម័ត"
            )
        else:
            text = (
                "Loan Overview:\n"
                "- Loan Amount: USD 500 – 20000 Up to 06 times of gross salary\n"
                "- Loan Term: Up to 36 months\n"
                "- Currency: KHR & USD\n"
                "- Interest Rate: Up to 18% per annum\n"
                "- Repayment Options:\n"
                "  1. Fixed principal and interest (Equal Principal Payment)\n"
                "  2. Fixed principal + Fixed interest (Fixed Payment)\n"
                "- Processing Fee: 1% of approved amount"
            )
    elif query.data == 'loan_eligibility':
        if language == 'km':
            text = (
                "លក្ខណៈសម្បត្តិ:\n"
                "- អ្នកដាក់ពាក្យត្រូវតែជាកូនប្រុសកូនស្រីខ្មែរតែប៉ុណ្ណោះ\n"
                "- អាយុ 18-65 ឆ្នាំ\n"
                "- មានគណនីប្រាក់បៀវត្សន៍នៅ FTB"
            )
        else:
            text = (
                "Eligibility:\n"
                "- Applicant must be Cambodian citizen only\n"
                "- Age 18-65 years old\n"
                "- Have payroll account with FTB"
            )
    elif query.data == 'loan_documents':
        if language == 'km':
            text = (
                "ឯកសារត្រូវការ:\n"
                "- បំពេញសំណុំបែបបទដាក់ពាក្យសុំឥណទាន\n"
                "- ឯកសាររបស់អ្នកខ្ចីប្រាក់និងអ្នកខ្ចីបន្ថែម\n"
                "- សៀវភៅគ្រួសារ\n"
                "- ឯកសារអាចបញ្ជាក់ប្រាក់ចំណូល រួមមាន កិច្ចសន្យាការងារ "
                "លិខិតបញ្ជាក់/បញ្ជាក់ អត្តសញ្ញាណបុគ្គលិក\n"
                "- ឯកសារគាំទ្រផ្សេងទៀតតាមការស្នើសុំពី FTB"
            )
        else:
            text = (
                "Required Documents:\n"
                "- Fill Loan application Form\n"
                "- Identity document of borrower and co-borrower\n"
                "- Family book\n"
                "- Income supporting documents including employment contract, "
                "verification/confirmation letter, staff ID\n"
                "- Other supporting documents subject to FTB's requirements"
            )

    keyboard = [
        [InlineKeyboardButton("Overview", callback_data='loan_overview')],
        [InlineKeyboardButton("Eligibility", callback_data='loan_eligibility')],
        [InlineKeyboardButton("Required Documents", callback_data='loan_documents')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text=text, reply_markup=reply_markup)

def loan_info_handler():
    return CommandHandler('loan_info', loan_info_start)

def loan_info_callback_handler():
    return CallbackQueryHandler(loan_info_callback, pattern='^loan_')