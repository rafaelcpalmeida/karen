import os
import random

import discord
from dotenv import load_dotenv

load_dotenv(encoding='utf8')

TOKEN = os.getenv('DISCORD_TOKEN')
BANNED_SENTENCES = os.getenv('BANNED_SENTENCES')
RESPONSES = os.getenv('RESPONSES')
EMOJIS = os.getenv('EMOJIS')

BANNED_SENTENCES = BANNED_SENTENCES.split(",")
RESPONSES = RESPONSES.split(",")
EMOJIS = EMOJIS.split(",")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    received_message = message.content.lower()
    if any(map(received_message.__contains__, BANNED_SENTENCES)):
        response = random.choice(RESPONSES).replace("[PLACEHOLDER]", next(substring for substring in BANNED_SENTENCES
                                                                          if substring in received_message))
        emoji = random.choice(EMOJIS)

        await message.delete()
        await message.channel.send(f"<@{message.author.id}>, {response} {emoji}")


client.run(TOKEN)
