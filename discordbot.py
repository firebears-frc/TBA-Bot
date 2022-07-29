from constants import _DiscordAUTH, _DISCORDCHANNELID
from discord.ext.commands import Bot
import time, asyncio

BOT_PREFIX = ["."]

def setup():
    global client
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


async def start():
    global mainChannel
    mainChannel = client.get_channel(_DISCORDCHANNELID)
    if(mainChannel == None):
        print("Main Channel Is Non Exsistant...")
        return

    print(mainChannel.name)
    await mainChannel.send('Im Up & Active! \n')


async def sendMessage(STR):
    mainChannel.send(STR)



client.run(_DiscordAUTH)