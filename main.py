import discord
from discord.app_commands import commands

import aternos_bot

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    aternos_bot.my_server.fetch()

    if message.author == client.user:
        return

    if message.content == "/start":
        aternos_bot.my_server.start()
        await message.channel.send("El server se prendio. 🔥🔥🔥👌👈")
    elif message.content == "/stop":
        aternos_bot.my_server.stop()
        await message.channel.send("El server se apago. 😕😕")
    elif message.content == "/status":
        status = aternos_bot.my_server.status
        await message.channel.send(f"El status es: {status}")

client.run('MTEzODk0Mzk4OTgzMjI0MTE3Mg.G5TnH0.pJBdNqkYLcX6vtsZBpavqrcJHQPoDyrWFo-BVk')
