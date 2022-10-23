import os
import discord
from discord.ext import commands
from numpy import random

bot = commands.Bot(command_prefix="$")
client = discord.Client()

name = ["Prinz", "PRINZ", "Eugen", "EUGEN", "prinz", "eugen"]


def seed_array():
    seed = list(range(0, 99))
    random.shuffle(seed)

    return seed


@bot.event
async def on_ready():
    print("I'm {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    if any(word in msg for word in name):
        await message.channel.send("Tg hein")

    await bot.process_commands(message)


Bot_token = os.environ["PE_MDP"]
bot.run(Bot_token)
# bot.run(os.getenv(Bot_token))

client.run(Bot_token)
