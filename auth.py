python3 -m pip install python-telegram-bot==20.7
export TELEGRAM_BOT_TOKEN="ВАШ_ТОКЕН_ОТ_BotFather"
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)

# Если не хотите использовать переменную окружения, замените None строкой с токеном:
# TOKEN = "ПОДСТАВЬТЕ_СЮДА_СВОЙ_ТОКЕН"
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	user = update.effective_user
	text = f"Привет, {user.first_name}!\nВаш Telegram ID: {user.id}"
	await update.message.reply_text(text)

def main() -> None:
	token = TOKEN
	if not token:
		raise RuntimeError("Не найден токен. Установите TELEGRAM_BOT_TOKEN или впишите токен в коде в переменную TOKEN.")
	app = Application.builder().token(token).build()
	app.add_handler(CommandHandler("start", start))
	app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
	main()
