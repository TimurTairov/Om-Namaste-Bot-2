from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from config import Token


bot = Bot(Token)
dp = Dispatcher(bot)

NAMASTE = """ намасте 🙏

Добро пожаловать в наш чат!

Ознакомьтесь с правилами чата по ссылке ниже:
⬇️⬇️⬇️"""
PRAVILA_CHATA = f'<a href="https://telegra.ph/PRAVILA-CHATA-04-17-19">ПРАВИЛА ЧАТА</a>'

# inline keyboards
ikb = InlineKeyboardMarkup()
ib2 = InlineKeyboardButton(text='Подписаться на Канал',
                           url='https://t.me/mdc_ShaktiMa')
ib1 = InlineKeyboardButton(text='ПРАВИЛА ЧАТА',
                           url='https://telegra.ph/PRAVILA-CHATA-04-17-19')
ib3 = InlineKeyboardButton(text='YouTube',
                           url='https://www.youtube.com/@ShaktiMA_MDC')
ib4 = InlineKeyboardButton(text='Сайт традиции Адвайта Сиддхов',
                           url='https://www.advayta.org')
ikb.add(ib2).add(ib3).add(ib4)

ikb1 = InlineKeyboardMarkup()
ib5 = InlineKeyboardButton(text='Пожертвовать',
                           url='https://yoomoney.ru/to/4100118169971120')
ikb1.add(ib5)


@dp.message_handler(content_types = ['new_chat_members', 'left_chat_member'])
async def delete(message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message):
    first_name = message.new_chat_members[0].first_name
    last_name = message.new_chat_members[0].last_name
    msg = await bot.send_message(message.chat.id, "Ом " + first_name + " " + last_name + NAMASTE +  "\n" + PRAVILA_CHATA,
                                 parse_mode='HTML', disable_web_page_preview=True, reply_markup=ikb)
    await asyncio.sleep(1080)
    await bot.delete_message(message.chat.id, msg.message_id)
    # await bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(first_name))
    # await bot.send_message(message.chat.id, "@" + str(message.from_user.username) + " Ом, Намасте. Добро пожаловать в чат!")




# @bot.message_handler(content_types=util.content_type_service)
# def delall(message):
#     bot.delete_message(message.chat.id,message.message_id)


if __name__ == "__main__":
    executor.start_polling(dp)
