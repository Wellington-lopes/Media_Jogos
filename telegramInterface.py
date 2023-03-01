from os import getenv
from dotenv import load_dotenv
from pyrogram import Client
from asyncio import run

import NBA
import futebol
import json

load_dotenv()

app = Client(
    'Mediasesportivas_bot',
    api_id = getenv('TELEGRAM_APP_ID'),
    api_hash = getenv('TELEGRAM_API_HASH'),
    bot_token = getenv('TELEGRAM_BOT_TOKEN')
)


async def main():
    user1 = 'Libianno'
    user2 = 'pitbulldaCC'

    liga, matches = NBA.main()
    strMaches = json.dumps(matches, indent=2)

    await app.start()
    await app.send_message(user1, liga)
    await app.send_message(user1, strMaches)
    #await app.send_message(user2, liga)
    #await app.send_message(user2, strMaches)

    run = futebol.main()
    try:
        while 1:

            liga, rodada, matches = next(run)
            strMaches = json.dumps(matches, indent=2)

            await app.send_message(user1, liga)
            await app.send_message(user1, rodada)
            await app.send_message(user1, strMaches)

    except StopIteration:
        pass

    await app.stop()

run(main())

