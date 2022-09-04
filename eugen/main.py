import os
import discord
import requests
import json
from discord.ext import commands
from keep_alive import keep_alive
import numpy
from numpy import random
from AL import al_incrpush


bot = commands.Bot(command_prefix='$')
client = discord.Client()

name = ["Prinz", "PRINZ", "Eugen", "EUGEN", "prinz", "eugen"]


def seed_array():
  seed = list(range(0,99))
  random.shuffle(seed)

  return(seed)




def get_tag(nub):
  #tag = requests.get("https://gelbooru.com/index.php?page=dapi&s=tag&q=index&api_key=anonymous&user_id=9455&json=1")
  tag = requests.get("https://danbooru.donmai.us/tags.json?search[category]=0&limit=100")
  
  tag_data = json.loads(tag.text)


  tl = 20 #####TAG LIMIT######


  tag_lenght = 0
  tag_list = "Dessine: "

  if nub > tl :
    nub = tl
    a = "Limite de tag: "
    b = "\nDessine: "

    tag_list = a + str(tl) + b


  seed = seed_array()
  i=0
  while tag_lenght < nub:
    
    tag_raw = tag_data[seed[i]]
    i += 1
    if tag_raw["category"] == 0:
      tag_list = tag_list +"  "+ tag_raw["name"]
      tag_lenght += 1

  return(tag_list)





Bot_token = os.environ['PE_MDP']



@bot.event
async def on_ready():
    print("I'm {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content


    if any(word in msg for word in name) :
      await message.channel.send("Tg hein") 

    await bot.process_commands(message)

@bot.command()
async def hentai(ctx, arg: int):
    await ctx.channel.send(get_tag(arg))

@bot.command()
async def test(ctx, arg):
    #al_incrpush()
    await ctx.channel.send(arg)



    
keep_alive()

bot.run(Bot_token)
#bot.run(os.getenv(Bot_token))

client.run(Bot_token)
