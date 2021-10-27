import discord
import os
import botwide_data as data
import commands as commands
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
    print('\nGEX GEX GEX GEX GEX GEX GEX GEX GEX GEX GEX')
    print('gex bot is online 😎 *dramatic music plays*')


@client.event
async def on_message(message):
    # Protect against overgex!!!!!!!!!!
    if "gex hustle" in message.content.lower():
      await message.channel.send("Gexnormal Pills")

    # Stops the bot from replying to it's own messages
    if message.author == client.user:
        return

    commands.user_commands(message)

    # gex combo (TEMPORTARY)
    if message.content.lower() == "g" and data.gex_combo == 0:
      data.gex_combo = 1
    elif message.content.lower() == "e" and data.gex_combo == 1:
      data.gex_combo = 2
    elif message.content.lower() == "x" and data.gex_combo == 2:
      data.gex_combo = 0
      data.gex += 69
      await message.channel.send("MEGA GEX COMBO, +69 Gex!")
    else:
      data.gex_combo = 0

    # Increase gex amount (TEMPORARY)
    if message.content.lower() == "gex":
      data.gex += 1
      await message.channel.send('+1 Gex')


keep_alive()

client.run(os.getenv('TOKEN'))
