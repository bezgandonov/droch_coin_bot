from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.tokens import BOT_TOKEN
from config.keyboards import main_keyboard
import db_helper

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Дрочкоин кафй', reply_markup=main_keyboard)


@dp.callback_query_handler(lambda query: query.data == 'balance_check')
async def balance_check(callback_query: types.CallbackQuery):
    balance = db_helper.balance_check(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, f'у вас осталось {balance} дрочкоинов🤪🤫👀😋')


class DRC_manipulation(StatesGroup):
    add = State()
    remove = State()

@dp.callback_query_handler(lambda query: query.data.startswith('change_balance'))
async def change_balance(callback_query: types.CallbackQuery):
    if callback_query.data.split(':')[1] == 'add':
        await bot.send_message(callback_query.from_user.id, 'сколько дрочкоинов добавить?')
        await DRC_manipulation.add.set()
    elif callback_query.data.split(':')[1] == 'remove':
        await bot.send_message(callback_query.from_user.id, 'сколько дрочкоинов выдрочили из себя?')
        await DRC_manipulation.remove.set()

@dp.message_handler(state=DRC_manipulation.add)
async def add_drochcoin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        db_helper.manipulate_wallet(message.from_user.id, message.text, True)
        await bot.send_message(message.from_user.id, 'успешно добавили')
    else:
        await bot.send_message(message.from_user.id, 'иди нахуй')
    await state.finish()

@dp.message_handler(state=DRC_manipulation.remove)
async def remove_drochcoin(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        db_helper.manipulate_wallet(message.from_user.id, message.text, False)
        await bot.send_message(message.from_user.id, 'успешно выдрочено🤩🤭🤗😳')
    else:
        await bot.send_message(message.from_user.id, 'иди нахуй')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
