import os
import logging
from telegram.ext import CommandHandler, Updater

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Obtener token y chat_id del entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
TEST_CHAT_ID = os.getenv("TEST_CHAT_ID")

# Crear instancia del bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handler para /start
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text="¡Hola! Bot activado correctamente. Te avisaré si hay estrenos indios.")

# Añadir handler
dispatcher.add_handler(CommandHandler("start", start))

# Iniciar el bot
if __name__ == "__main__":
    logging.info("Bot iniciado")
    updater.start_polling()

    # Enviar mensaje de prueba después de que polling esté activo
    if TEST_CHAT_ID:
        try:
            updater.bot.send_message(chat_id=TEST_CHAT_ID, text="🎬 El bot está funcionando correctamente. ¡Listo para buscar estrenos!")
        except Exception as e:
            logging.error(f"Error al enviar mensaje de prueba: {e}")

    updater.idle()
