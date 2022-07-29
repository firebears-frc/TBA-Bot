from constants import _DiscordAUTH, _DISCORDCHANNELID
import discord
from discord.ext.commands import Bot
import time, asyncio

BOT_PREFIX = ["."]
client = Bot(command_prefix=BOT_PREFIX)
@client.event
async def on_message(message):
    if message.author == client.user:
        return




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await start()
    while True:
        currentTime = time.strftime("%M%S", time.gmtime(time.time()))
        if currentTime == "30:00":
            await start()
        await asyncio.sleep(1)


async def start():
    global mainChannel
    mainChannel = client.get_channel(_DISCORDCHANNELID)
    print(mainChannel.name)
    await client.send_message(mainChannel, "Starting countdown", tts = True)



client.run(_DiscordAUTH)