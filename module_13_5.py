import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
token = "0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
kbd = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Рассчитать'),
    KeyboardButton(text='Информация'))
@dp.message_handler(text=['Рассчитать'])
async def set_age(message):
    await message.answer('Введите свой возраст (лет):')
    await UserState.age.set()
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        await state.update_data(age=float(message.text))
    except ValueError:
        await message.answer('Введите свой возраст (лет):')
        await UserState.age.set()
    else:
        await message.answer('Введите свой рост (см):')
        await UserState.growth.set()
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        await state.update_data(growth=float(message.text))
    except ValueError:
        await message.answer('Введите свой рост (см):')
        await UserState.growth.set()
    else:
        await message.answer('Введите свой вес (кг):')
        await UserState.weight.set()
@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        await state.update_data(weight=float(message.text))
    except ValueError:
        await message.answer('Введите свой вес (кг):')
        await UserState.weight.set()
    else:
        data = await state.get_data()
        REE = 10 * data['weight'] \
            + 6.25 * data['growth'] \
            - 5 * data['age'] + 5
        await message.answer(
            f'Ваша суточная норма {round(REE, 2)} килокалорий')
        await state.finish()
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(
        'Привет! Я бот помогающий вашему здоровью.'
        ' Нажмите "Рассчитать", чтобы узнать вашу суточную норму'
        ' потребления килокалорий', reply_markup=kbd)
@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer(
        'Данный бот подсчитывает норму потребления калорий для мужчин по'
        ' упрощённой формуле Миффлина - Сан Жеора'
        ' (https://www.calc.ru/Formula-Mifflinasan-Zheora.html).')
@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)