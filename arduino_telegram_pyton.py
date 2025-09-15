from telegram.ext import Updater, MessageHandler, Filters
import serial
import time

# Token del bot
TOKEN = "8344054614:AAFUukJS84ydaLZzsugMRZHqHKGo0a2j7Sk"

# Configuración del puerto serial
arduino = serial.Serial('COM3', 9600)
time.sleep(2)

# Función que maneja los mensajes
def manejar_mensaje(update, context):
    texto = update.message.text.lower()
    chat_id = update.message.chat_id
    print(f"Mensaje recibido: {texto}")

    if "enciende" in texto:
        arduino.write(b"enciende\n")
        context.bot.send_message(chat_id=chat_id, text="💡 LED encendido")
    elif "apaga" in texto:
        arduino.write(b"apaga\n")
        context.bot.send_message(chat_id=chat_id, text="🌑 LED apagado")
    else:
        context.bot.send_message(chat_id=chat_id, text="⚠️ Comando no reconocido")

# Configuración del bot
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, manejar_mensaje))

# Iniciar el bot
print("🤖 Bot activo. Esperando mensajes...")
updater.start_polling()
updater.idle()