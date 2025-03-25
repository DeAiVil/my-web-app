import os
import pandas as pd
import numpy as np
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

# создайте экземпляр приложения
application = Application.builder().token("8130756124:AAHwb-DRaY-f9ELWDSlOAH6LMnj04nR8tiI").build()

# функции стартового меню
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Информация о клубе", web_app=WebAppInfo(url="https://deaivil.github.io/my-web-app/info.html")),
            InlineKeyboardButton("Подобрать игру", web_app=WebAppInfo(url="https://yourdomain.com/booking")),
        ],
        [
            InlineKeyboardButton("Каталог игр", web_app=WebAppInfo(url="https://yourdomain.com/catalog")),
            InlineKeyboardButton("Цены", callback_data="prices"),  # Добавлена кнопка с callback_data
        ],
        [
            InlineKeyboardButton("Бронирование", web_app=WebAppInfo(url="https://yourdomain.com/recommendations")),
            InlineKeyboardButton("Связаться с администратором", callback_data="contact"),  # Добавлена кнопка с callback_data
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в клуб виртуальной реальности!", reply_markup=reply_markup)

# обработчик для кнопки "Цены"
async def prices(update: Update, context: CallbackContext):
    await update.callback_query.answer(text="Обрабатываю запрос...")  # Предварительный ответ
    await update.callback_query.edit_message_text("Цены на наши услуги:\n- 1 час игры: 500 рублей\n- 2 часа игры: 900 рублей")

# обработчик для кнопки "Связаться с администратором"
async def contact(update: Update, context: CallbackContext):
    await update.callback_query.answer()  # Ответ на запрос callback
    await update.callback_query.edit_message_text("Вы можете связаться с администратором по номеру: +7 123 456 78 90")

# Добавление обработчиков в основной код
application.add_handler(CallbackQueryHandler(prices, pattern="prices"))
application.add_handler(CallbackQueryHandler(contact, pattern="contact"))
application.add_handler(CommandHandler("start", start))

# Запуск бота
def main():
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
