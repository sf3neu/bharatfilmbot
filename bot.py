
import os
import requests
import time
import logging
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtener token del entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Crear instancia del bot
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# Respuesta a /start
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="¡Hola! Bot activado correctamente. Te avisaré si hay estrenos indios.")

# Añadir handler
dispatcher.add_handler(CommandHandler("start", start))

# Iniciar el bot
if __name__ == "__main__":
    logging.info("Bot iniciado")
    updater.start_polling()
    updater.idle()
