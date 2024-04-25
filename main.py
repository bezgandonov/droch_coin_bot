from aiogram import Dispatcher, Bot, executor, types
from config.tokens import BOT_TOKEN
from config.keyboards import main_keyboard

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.chat.id, 'Дрочкоин кафй', reply_markup=main_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
