import os
import discord
import requests
import json
from discord.ext import commands
#import datetime
import numpy
from numpy import random
from replit import db
from datetime import datetime

###URL DANBOORU####
# compte DANBOORU utilisateur: albot
#                 mot de passe: albot
# WEEEEEEEEEEEEEB
# https://danbooru.donmai.us/post_appeals.json?search[name_matches]=*(azur_lane)&search[category]=4&limit=1000

def filter_tags(tags):
  if tags.find("(azur_lane)") != -1 and tags.count('(') < 2 and tags.find("manjuu") == -1 :
    return True
  else:
    return False 


def al_incrpush():
  load_limit = 100 ####incrementaly load this number of posts 
  post = requests.get("https://danbooru.donmai.us/posts.json?tags=*azur_lane&limit={}".format(load_limit)) 
  post_data = json.loads(post.text)

  
  load_limit -= 1
  i = 0 
  while i <= load_limit :  
    post_raw = post_data[i]
    post_time = post_raw["created_at"]
    #print(post_time)
    year = post_time[0:4]
    #print(year)
    month = post_time[5:7]
    #print(month)
    day = post_time[8:10]
    #print(day)
    hour = post_time[11:13]
    #print(hour)
    minute = post_time[14:16]
    #print(minute)
    second = post_time[17:19]
    #print(second)
    microsecond = post_time[20:23]
    #print(microsecond)
    timestamp = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond))
    #print(timestamp)
    tags = post_raw["tag_string"].split()
    #print(tags)
    ship_name_filter = filter(filter_tags,tags)
    for tag in ship_name_filter:
      #print(tag)
      ship_name = tag


    
    #print(ship_name)
    i += 1

    db[timestamp.strftime("%Y/%m/%d %H:%M:%S:%f")] = [ship_name]

  #print(tags)
  return()

def read_db():
  for element in db:
    print(db[element][0])



#read_db()
# al_incrpush()

#db.clear()




# # datetime(year, month, day, hour, minute, second, microsecond)
# b = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print(b)