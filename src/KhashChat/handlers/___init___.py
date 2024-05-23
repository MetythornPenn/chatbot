# Importing command functions from other modules
from telegram.ext import dispatcher, CommandHandler

from handler.start import command as start_command
from .help import command as help_command
from .advice import command as advice_command

# Adding command handlers to the dispatcher
dispatcher.add_handler(CommandHandler("start", start_command))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CommandHandler("advice", advice_command))
dispatcher.add_handler(CommandHandler("budget", budget_command))

