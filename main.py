import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


@client.event
async def on_message(message):
    if message.author != client.user:
        await message.channel.send(message.content[::-1])


keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
if token is None:
    raise ValueError("DISCORD_BOT_SECRET environment variable not set")
client.run(token)
