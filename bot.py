
import os
import logging
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, CallbackContext

# Configurar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Leer variables de entorno
TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Crear Flask app
app = Flask(__name__)

# Crear bot y dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

# Ruta raíz opcional para evitar 404 en "/"
@app.route("/")
def index():
    return "Bot en funcionamiento."

# Handler para /start
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola! Bot activado correctamente vía webhook. Te avisaré si hay estrenos indios.")

dispatcher.add_handler(CommandHandler("start", start))

# Ruta para recibir las actualizaciones de Telegram
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# Configurar webhook y arrancar servidor
if __name__ == "__main__":
    bot.set_webhook(f"{WEBHOOK_URL}/{TOKEN}")
    app.run(host="0.0.0.0", port=10000)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
