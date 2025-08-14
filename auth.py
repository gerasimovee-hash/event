import os
import sys
import logging


TOKEN = "8163748588:AAEjZzAV4kqcWtEhtZWluooavhYlJehTMyw"  

try:
	from telegram import Update
	from telegram.ext import Application, CommandHandler, ContextTypes
except Exception as e:
	print("Не найдена библиотека python-telegram-bot.\nУстановите: pip install python-telegram-bot==20.7")
	sys.exit(1)

logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


def _get_token() -> str:
	token = TOKEN.strip() or os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN")
	if not token:
		token = input("Введите TELEGRAM_BOT_TOKEN: ").strip()
	if not token:
		raise RuntimeError("Токен не задан. Вставьте в переменную TOKEN или задайте TELEGRAM_BOT_TOKEN.")
	return token


async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	user = update.effective_user
	text = f"Привет, {user.first_name}!\nВаш Telegram ID: {user.id}"
	if update.message:
		await update.message.reply_text(text)
	elif update.callback_query:
		await update.callback_query.message.reply_text(text)


def start() -> None:
	token = _get_token()
	app = Application.builder().token(token).build()
	app.add_handler(CommandHandler("start", cmd_start))
	logging.info("Бот запущен. Нажмите Ctrl+C для остановки.")
	app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
	start()
