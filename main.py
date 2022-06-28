import requests
import re
import discord


ersin = discord.Client()
koydummuyersin = requests.session()
nsfwchannel = #your channel id
tokenDDDD = "your bot token"

@ersin.event
async def on_ready():
 print('bot is ready')


def ass():
 d = koydummuyersin.get('https://api.waifu.im/random/?selected_tags=ass')
 f = (re.split('https://cdn.waifu.im/', str(d.text))[1].split('\"')[0])
 h = (f"https://cdn.waifu.im/{f}")
 return(h)

@ersin.event
async def on_message(message):
  if message.author == ersin.user:
    return

  msg = message.content

  if msg.startswith('ass'):
    a = ass()
    channel = ersin.get_channel(nsfwchannel)
    await channel.send(a)    
          
ersin.run(tokenDDDD)
