from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_keyboard = InlineKeyboardMarkup()
main_keyboard.add(InlineKeyboardButton(text='просмотреть баланс', callback_data='balance_check'))
main_keyboard.add(InlineKeyboardButton(text='прибавить к балансу', callback_data='change_balance:add'))
main_keyboard.add(InlineKeyboardButton(text='отнять от баланса', callback_data='change_balance:remove'))
