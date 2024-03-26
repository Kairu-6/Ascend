import telethon
from misc import new_cat

api_id = 21745398
api_hash = "381e0a5b910b5533b40ae1b2e3b50364"
bot_token = "7118642893:AAGaLXcohyum0ExrLL8xNC3XHdXNUiR5nQM"
apicat = "live_bNM0ztnyqxNWhFDEgaYFOa2tfxjByPvkdXZQacdnmlBptflIFW1G6dGr41UbXmQw"

kai = telethon.TelegramClient("kai", api_hash=api_hash, api_id=api_id)
bot = telethon.TelegramClient("bot", api_id=api_id, api_hash=api_hash).start(bot_token=bot_token)

async def maink():
    pass

@bot.on(telethon.events.NewMessage)
async def rawr(event):
    chat = await event.get_sender()
    if ("mew" in event.raw_text) and (event.sender_id == 2086959371):
        new_cat()
        await event.reply(file="mew.jpg")
    elif ("mew" in event.raw_text) and (event.sender_id != 2086959371):
        await event.reply("nuh uh")

with kai:
    kai.loop.run_until_complete(maink())

bot.run_until_disconnected()
