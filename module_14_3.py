import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                          InlineKeyboardMarkup, InlineKeyboardButton
import config
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
class UserState(StatesGroup):
    age = State()
    growth = State() 
    weight = State()
kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [KeyboardButton(text='Купить')]
    ], resize_keyboard=True
)
inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Рассчитать норму калорий',
                                 callback_data='calories'),
            InlineKeyboardButton(text='Формулы расчёта',
                                 callback_data='formulas')
        ]
    ]
)
goods_kb = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text='Product1',
                             callback_data='product_buying'),
        InlineKeyboardButton(text='Product2',
                             callback_data='product_buying'),
        InlineKeyboardButton(text='Product3',
                             callback_data='product_buying'),
        InlineKeyboardButton(text='Product4',
                             callback_data='product_buying')
    ]]
)
@dp.message_handler(text=['Рассчитать'])
async def send_inline_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        '10·вес(кг) + 6.25·рост(см) – 5·возраст(лет) + 5')
    await call.answer()
@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (лет):')
    await call.answer()
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
        # Resting energy expenditure
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
        ' потребления килокалорий', reply_markup=kb)
@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer(
        'Данный бот подсчитывает норму потребления калорий для мужчин по'
        ' упрощённой формуле Миффлина - Сан Жеора'
        ' (https://www.calc.ru/Formula-Mifflinasan-Zheora.html).')
@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for i in range(1, 5):
        await message.answer(f'Название: Product{i} | '
                             f'Описание: описание {i} | '
                             f'Цена: {i * 100}')
        with open(f'product{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:',
                         reply_markup=goods_kb)
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)