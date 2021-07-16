import configs
import logging

from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token = configs.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(is_admin=True, commands=["start"], commands_prefixx"!/")
asinc def cmd_ban(message: types.Message):

    await message.reply_to_message.reply("Привет!")
    
# echo
@dp.message_handler()
async def filter_message(message: types.Message):
    if "Привет" in message.text:
        await message.answer("Привет!")
    
# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)