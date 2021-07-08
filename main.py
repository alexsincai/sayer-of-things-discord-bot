import discord
from dotenv import load_dotenv
from os import environ

from bot_logic import parse

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} listening...")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("~"):
        msg = parse(message.content[1:])
        
        if msg is not None:
            await message.channel.send(msg)

        return


# https://discord.com/api/oauth2/authorize?client_id=862590420739293214&permissions=76800&scope=bot
client.run(environ.get("TOKEN"))
