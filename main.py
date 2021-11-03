import os
import random
import sys

import discord
from dotenv import load_dotenv

load_dotenv(encoding='utf8')

TOKEN = os.getenv('DISCORD_TOKEN') or None
if TOKEN is None:
    sys.exit("DISCORD_TOKEN not defined")
BANNED_SENTENCES = os.getenv('BANNED_SENTENCES') or None
if BANNED_SENTENCES is None:
    sys.exit("BANNED_SENTENCES not defined")
RESPONSES = os.getenv('RESPONSES') or None
if RESPONSES is None:
    sys.exit("RESPONSES not defined")
EMOJIS = os.getenv('EMOJIS') or None
if EMOJIS is None:
    sys.exit("EMOJIS not defined")
SALUTATIONS = os.getenv('SALUTATIONS') or None
if SALUTATIONS is None:
    sys.exit("SALUTATIONS not defined")

BANNED_SENTENCES = BANNED_SENTENCES.split(",")
RESPONSES = RESPONSES.split(",")
EMOJIS = EMOJIS.split(",")
SALUTATIONS = SALUTATIONS.split(",")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    emoji = random.choice(EMOJIS)

    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        response = random.choice(SALUTATIONS)
        await message.channel.send(f"<@{message.author.id}>, {response} {emoji}")

    received_message = message.content.lower()
    if any(map(received_message.__contains__, BANNED_SENTENCES)):
        response = random.choice(RESPONSES).replace("[PLACEHOLDER]", next(substring for substring in BANNED_SENTENCES
                                                                          if substring in received_message))

        await message.delete()
        await message.channel.send(f"<@{message.author.id}>, {response} {emoji}")


client.run(TOKEN)
