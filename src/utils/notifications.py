import os
from telegram import Bot
from telegram.error import TelegramError

# Токен бота и ID администратора — из переменных окружения
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_ID = int(os.getenv("TELEGRAM_USER_ID"))


async def send_admin_notification(balance):
    """Отправляет уведомление администратору."""
    b = balance[1:]
    balance_float = round(float(b), 2)
    
    bot = Bot(token=BOT_TOKEN)
    message_text = f'⚠️ Приложение: Ваш баланс равен {balance}! Пополните его на сайте openrouter.ai.'
    
    async with bot:  # инициализирует и корректно закрывает сессию
        try:
            if balance_float <= 0.00:
                print("Уведомление отправлено.")                
                return await bot.send_message(chat_id=ADMIN_ID, text=message_text)
        except TelegramError as e:
                return print(f"Ошибка отправки уведомления")