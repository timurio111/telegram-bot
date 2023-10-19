from aiogram import Bot, Dispatcher, executor, filters, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_dialog import DialogRegistry
from datetime import datetime

import markups

API_TOKEN = "YOUR_TOKEN_HERE"

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
PHOTOS_AMOUNT = 0  # YOUR AMOUNT
VIDEOS_AMOUNT = 0  # YOUR AMOUNT
photosCounter = 0  # YOUR AMOUNT
videosCounter = 0  # YOUR AMOUNT

registry = DialogRegistry(dp)


def update_counter(current_amount: int, global_amount: int) -> int:
    return (current_amount + 1) % (global_amount + 1) + 1 * (current_amount == global_amount)


async def send_video(call: types.callback_query.CallbackQuery) -> None:
    global videosCounter
    video_format = "mp4"  # YOUR FORMAT HERE
    media = types.MediaGroup()
    media.attach_video(types.InputFile(f"data/videos/{videosCounter}.{video_format}"))
    videosCounter = update_counter(videosCounter, VIDEOS_AMOUNT)
    await bot.send_media_group(chat_id=call.message.chat.id, media=media)
    await call.message.answer("Your text for videos here", reply_markup=markups.videos_markup)


async def send_photo(call: types.callback_query.CallbackQuery) -> None:
    global photosCounter
    media = types.MediaGroup()
    media.attach_photo(types.InputFile(f'data/photos/{photosCounter}.jpg'))
    photosCounter = update_counter(photosCounter, PHOTOS_AMOUNT)
    await bot.send_media_group(chat_id=call.message.chat.id, media=media)
    await call.message.answer("Your text for photos here", reply_markup=markups.photos_markup)


@dp.message_handler(filters.CommandStart())
async def start(m: Message) -> None:
    await m.reply(
        "Your /start reply")
    await bot.send_sticker(m.from_user.id,
                           sticker="Your /start sticker id (optional)")
    await m.answer("Your text to show markups")


@dp.message_handler()
async def info(m: Message) -> None:
    await m.reply("Your text before markups", reply_markup=markups.main_markup)


@dp.callback_query_handler()
async def callback(call: types.callback_query.CallbackQuery) -> None:
    global photosCounter
    global videosCounter
    time_now = datetime.now()
    current_time = time_now.strftime("%H:%M:%S")
    if call.data == "Your call_data for photos" or call.data == "Your call_data for next photo":
        # Prints logs to terminal
        print(f"{call.data}: {photosCounter}, time: {current_time}")
    elif call.data == "Your call_data for videos" or call.data == "Your call_data for next video":
        # Prints logs to terminal
        print(f"{call.data}: {videosCounter}, time: {current_time}")
    else:
        print(f"{call.data}, time: {current_time}")
    callback_text = call.data
    match callback_text:
        case "Your call_back text":
            await call.message.answer("Your message answer", reply_markup=markups.main_markup)
        case "Your call_back text for photo":
            await send_photo(call)
        case "Your call_back text for video":
            await send_video(call)
        case "Your call_back text for next photo":
            await send_photo(call)
        case "Your call_back text for next video":
            await send_video(call)
        case "Your call_back text to go back to main markup":
            photosCounter, videosCounter = 1, 1
            await call.message.answer("Your text when user gets back to main markup", reply_markup=markups.main_markup)
        case "Your call_back text":
            await bot.send_sticker(call.from_user.id,
                                   sticker="Your sticker id")
            await call.message.answer("Your message answer", reply_markup=markups.first_text_markup)
        case "Your call_back text":
            await call.message.answer("Your message answer", reply_markup=markups.main_markup)
        case "Your call_back text for voice message":
            voice = types.InputFile("data/voice/voice.ogg")
            await bot.send_voice(chat_id=call.message.chat.id, voice=voice)
            await call.message.answer("Your text when user gets back to main markup", reply_markup=markups.main_markup)

        case "Your call_back text for chain of markups (first)":
            await call.message.answer("Your message answer", reply_markup=markups.second_text_markup)
        case "Your call_back text for chain of markups (second)":
            await call.message.answer("Your message answer", reply_markup=markups.third_text_markup)
        case "YYour call_back text for chain of markups (third)":
            await call.message.answer("Your message answer", reply_markup=markups.fourth_text_markup)
        case "Your call_back text for chain of markups (fourth)":
            await call.message.answer("Your message answer", reply_markup=markups.main_markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
