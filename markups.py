from aiogram import types

main_markup = types.InlineKeyboardMarkup()
main_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
main_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
main_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
main_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
main_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
main_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))

videos_markup = types.InlineKeyboardMarkup()
videos_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
videos_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))

first_text_markup = types.InlineKeyboardMarkup()  # Start a chain of markups
first_text_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))

second_text_markup = types.InlineKeyboardMarkup()
second_text_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))

third_text_markup = types.InlineKeyboardMarkup()
third_text_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))

fourth_text_markup = types.InlineKeyboardMarkup()
fourth_text_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))

photos_markup = types.InlineKeyboardMarkup()
photos_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
photos_markup.add(types.InlineKeyboardButton("Your text here", callback_data="Your callback_data"))
