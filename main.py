import asyncio
import json
import logging
import os
from random import randrange
from aiogram import Bot, Dispatcher, types

import inline_keyboard

log = logging.getLogger(__name__)
log.setLevel(os.environ.get('LOGGING_LEVEL', 'INFO').upper())




async def start(message: types.Message):
    await message.answer(text='Hello, {}!'.format(message.from_user.first_name),
                         reply_markup=inline_keyboard.START)

async def help(message: types.Message):
    await message.answer(text='У меня есть следующие функции:\n1)/start\n2)/help\n3)/happyny\n4)Я повторяю за вами текст\n5)кнопочка с ТОЧНО НЕ рикроллом\n6)Кнопочка в старте которая вызывает хелп\n',
                         reply_markup=inline_keyboard.HELP)


async def hny(message: types.Message):    
    await message.answer(text='С новым годом!')

async def echo(message: types.Message):
    await message.answer(message.text)


async def register_handlers(dp: Dispatcher):

    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(hny, commands=['happyny'])
    dp.register_message_handler(echo)
   
    log.debug('Handlers are registered.')


async def process_event(event, dp: Dispatcher):

    update = json.loads(event['body'])
    log.debug('Update: ' + str(update))

    Bot.set_current(dp.bot)
    update = types.Update.to_object(update)
    await dp.process_update(update)


async def handler(event, context):
    
    bot = Bot(os.environ.get('BOT_TOKEN'))
    dp = Dispatcher(bot) 
    @dp.callback_query_handler(text='help')
    async def process_callback_help(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text='У меня есть следующие функции:\n1)/start\n2)/help\n3)/happyny\n4)Я повторяю за вами текст\n5)кнопочка с ТОЧНО НЕ рикроллом\n6)Кнопочка в старте которая вызывает хелп\n',
            reply_markup=inline_keyboard.HELP
        )   

    await register_handlers(dp)
    await process_event(event, dp)

    return {'statusCode': 200, 'body': 'ok'}
