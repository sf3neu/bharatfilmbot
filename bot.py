
import os
import logging
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtener token del entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
TEST_CHAT_ID = os.getenv("TEST_CHAT_ID")

# Crear instancia del bot
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# Handler para /start
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="¡Hola! Bot activado correctamente. Te avisaré si hay estrenos indios.")

# Añadir handler
dispatcher.add_handler(CommandHandler("start", start))

# Enviar mensaje de prueba al iniciar
if TEST_CHAT_ID:
    try:
        bot = Bot(token=TOKEN)
        bot.send_message(chat_id=TEST_CHAT_ID, text="🎬 El bot está funcionando correctamente. ¡Listo para buscar estrenos!")
    except Exception as e:
        logging.error(f"Error al enviar mensaje de prueba: {e}")

# Iniciar el bot
if __name__ == "__main__":
    logging.info("Bot iniciado")
    updater.start_polling()
    updater.idle()
