import discord
import os
import random
import gex as gex
from keep_alive import keep_alive

command_prefix = '!'

quotes = [
    "It's tail time",
    "GEX!!!",
    "Gex responsibly",
    "Have you ever heard of [[Hyperlink Blocked]]?",
    "Don't overgex!",
    "Gex Hustle",
    "Everyday I'm gexing",
    "Oh yeah. It’s tail time",
    "Taaaaiil tiiime",
    "Tltm",
    "Tale thyhme",
    "Iiits tail time",
    "TAIL TIME",
    "it's closing in",
    "it's 'hey all'",
    "Madden '08",
    "enter the Gecko",
    "I thought you were a vegan",
    "IT'S AWESOME BABY",
    "I'm not an RPG guy",
    "@everyone",
    "I love gex",
    "subscribe to dunkey son"
]

client = discord.Client()


@client.event
async def on_ready():
    print('\nGEX GEX GEX GEX GEX GEX GEX GEX GEX GEX GEX')
    print('gex bot is online 😎 *dramatic music plays*')


@client.event
async def on_message(message):
    if "gex hustle" in message.content.lower():
      await message.channel.send("Gexnormal Pills")

    if message.author == client.user:
        return

    if message.content.startswith(command_prefix + "name"):
      command_parts = message.content.split()
      await message.channel.send("I guess my name is " + command_parts[1] + " now ¯\_(ツ)_/¯")
      await message.guild.me.edit(nick=command_parts[1])

    if message.content == command_prefix + "fella":
      await message.channel.send(file=discord.File('fella.webp'))

    if message.content == command_prefix + "frog":
      await message.channel.send(file=discord.File('frog.png'))

    if message.content == command_prefix + "goodtime":
      await message.channel.send("party rockers in the house tonight!!!!!!")
      await message.channel.send(file=discord.File('Peter_Griffin.png'))
      await message.channel.send("peter giffin just wanna, get fat")

    if message.content == command_prefix + "imposter":
      await message.channel.send(file=discord.File('sussychung.png'))

    if message.content == command_prefix + "chungus":
      await message.channel.send(file=discord.File('chung.png'))

    if message.content == command_prefix + "isawyoudoit":
      await message.channel.send(file=discord.File('jerma/see you.jpg'))

    if message.content == command_prefix + "jerma":
      await message.channel.send(file=discord.File('jerma/sussy.png'))

    if message.content == command_prefix + "door":
      await message.channel.send("face reveal!!!")
      await message.channel.send(file=discord.File('a hecking door.jpg'))

    if message.content == command_prefix + "youtube":
      await message.channel.send("https://www.youtube.com/channel/UCK1VJI8Gyh6qfozmqezTHsg")

    if message.content == command_prefix + "fard":
      await message.channel.send("\*fard sound effect\*")

    if message.content == command_prefix + "autopill":
      await message.channel.send("Gexnormal pills")

    if message.content == command_prefix + "help":
      await message.channel.send("no")

    if message.content == command_prefix + "die":
      await message.channel.send("uno reverse card")

    if message.content == command_prefix + "quote":
      option = random.randint(0, len(quotes) - 1)
      await message.channel.send(quotes[option])

    if message.content == command_prefix + "gex":
      await message.channel.send("You have " + str(gex.gex) + " gex")

    if message.content.lower() == "g" and gex.gex_combo == 0:
      gex.gex_combo = 1
    elif message.content.lower() == "e" and gex.gex_combo == 1:
      gex.gex_combo = 2
    elif message.content.lower() == "x" and gex.gex_combo == 2:
      gex.gex_combo = 0
      gex.gex += 69
      await message.channel.send("MEGA GEX COMBO, +69 Gex!")
    else:
      gex.gex_combo = 0

    if message.content.lower() == "gex":
      gex.gex += 1
      await message.channel.send('+1 Gex')


keep_alive()

client.run(os.getenv('TOKEN'))
