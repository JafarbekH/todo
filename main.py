from aiogram import types, Bot, Dispatcher 
from aiogram.utils import executor  

token = '6216398955:AAFlhzmunHnaftZVAVkskqAskbYZtnYbbSo' 

bot = Bot(token=token) 
dp = Dispatcher(bot=bot) 

@dp.message_handler(commands='start')
async def start(msg: types.Message):
    await msg.answer('hello')


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)

