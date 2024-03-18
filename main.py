import logging

from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.errors import RPCError

from pyrogram.types import Message

from src import check_status, API_ID, API_HASH, BOT_TOKEN, create_funnel_db, check_triggers, change_funnel_status

logging.basicConfig(level=logging.INFO)

app = Client(
    name='pyrogram_userbot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


@app.on_message(filters=filters.command('start'))
async def start_funnel_handler(client: Client, message: Message) -> None:
    """Handler для запуска воронки при первом обращении пользователя к боту."""

    check_user = await create_funnel_db(message.from_user.id, 'alive')
    if check_user:
        chat_id = message.chat.id
        counter = 0
        intervals = {1: 360, 2: 2340, 3: 93600}
        while True:
            if counter == 3:
                await change_funnel_status(message.from_user.id, 'finished')
                break
            counter += 1
            await sleep(intervals[counter])
            if await check_status(message.from_user.id):
                break
            try:
                await client.send_message(chat_id=chat_id, text=f'Текст {counter}')
            except RPCError:
                await change_funnel_status(user_id=message.from_user.id, user_status='dead')
                break


@app.on_message()
async def triggers_funnel_handler(_, message: Message) -> None:
    """Handler для проверки новых сообщений пользователей на наличие слов-триггеров."""

    if await check_status(message.from_user.id) and await check_triggers(message.text):
        await change_funnel_status(message.from_user.id, 'finished')


def main():
    app.run()


if __name__ == '__main__':
    main()
