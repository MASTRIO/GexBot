import discord
import random
import botwide_data as data

command_prefix = "!"

async def user_commands(message):
    ## Emergency commands
    # Incase the medical proffesional isn't around and the bot is too lazy
    if message.content == command_prefix + "autopill":
        await message.channel.send("Gexnormal pills")

    ## Commands that do things
    # Change the bots nickname
    if message.content.startswith(command_prefix + "name"):
      command_parts = message.content.split()
      await message.channel.send("I guess my name is " + command_parts[1] + " now ¯\_(ツ)_/¯")
      await message.guild.me.edit(nick=command_parts[1])

    # Random quote
    if message.content == command_prefix + "quote":
      option = random.randint(0, len(data.quotes) - 1)
      await message.channel.send(data.quotes[option])

    # Show amount of gex
    if message.content == command_prefix + "gex":
      await message.channel.send("You have " + str(data.gex) + " gex")

    ## Image commands
    # Fart smells
    if message.content == command_prefix + "fella":
      await message.channel.send(file=discord.File('images/fella.webp'))

    # Jens kinda sussy
    if message.content == command_prefix + "frog":
      await message.channel.send(file=discord.File('images/frog.png'))

    # peter giffin had a good good good good time
    if message.content == command_prefix + "goodtime":
      await message.channel.send("party rockers in the house tonight!!!!!!")
      await message.channel.send(file=discord.File('images/Peter_Griffin.png'))
      await message.channel.send("peter giffin just wanna, get fat")

    # dun dun, dun dun dund udn dun dun dun, dun dun dun, dom dom
    if message.content == command_prefix + "imposter":
      await message.channel.send(file=discord.File('images/sussychung.png'))

    # big big chungus, big chungus, big chungus
    if message.content == command_prefix + "chungus":
      await message.channel.send(file=discord.File('images/chung.png'))

    # I know it was you, I saw you do it
    if message.content == command_prefix + "isawyoudoit":
      await message.channel.send(file=discord.File('images/see you.jpg'))

    # When the imposter is sus
    if message.content == command_prefix + "jerma":
      await message.channel.send(file=discord.File('jerma/sussy.png'))

    # OMG GUYS FACE REVEAL?!??!?!?!?!1?
    if message.content == command_prefix + "door":
      await message.channel.send("face reveal!!!")
      await message.channel.send(file=discord.File('images/a hecking door.jpg'))

    ## Message commands
    # Go subscribe right now
    if message.content == command_prefix + "youtube":
        await message.channel.send("https://www.youtube.com/channel/UCK1VJI8Gyh6qfozmqezTHsg")

    # PFOFOOBFBOBFBT
    if message.content == command_prefix + "fard":
        await message.channel.send("\*fard sound effect\*")

    # No seriously call the ambulance
    if message.content == command_prefix + "help":
        await message.channel.send("no")

    # why do you want Gex to die?
    if message.content == command_prefix + "die":
        await message.channel.send("uno reverse card")