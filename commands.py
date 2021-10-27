import discord
import random
import botwide_data as data

command_prefix = "!"

def user_commands(message):
    ## Emergency commands
    # Incase the medical proffesional isn't around and the bot is too lazy
    if message.content == command_prefix + "autopill":
        message.channel.send("Gexnormal pills")

    ## Commands that do things
    # Change the bots nickname
    if message.content.startswith(command_prefix + "name"):
      command_parts = message.content.split()
      message.channel.send("I guess my name is " + command_parts[1] + " now ¯\_(ツ)_/¯")
      message.guild.me.edit(nick=command_parts[1])

    # Random quote
    if message.content == command_prefix + "quote":
      option = random.randint(0, len(data.quotes) - 1)
      message.channel.send(data.quotes[option])

    # Show amount of gex
    if message.content == command_prefix + "gex":
      message.channel.send("You have " + str(data.gex) + " gex")

    ## Image commands
    # Fart smells
    if message.content == command_prefix + "fella":
      message.channel.send(file=discord.File('images/fella.webp'))

    # Jens kinda sussy
    if message.content == command_prefix + "frog":
      message.channel.send(file=discord.File('images/frog.png'))

    # peter giffin had a good good good good time
    if message.content == command_prefix + "goodtime":
      message.channel.send("party rockers in the house tonight!!!!!!")
      message.channel.send(file=discord.File('images/Peter_Griffin.png'))
      message.channel.send("peter giffin just wanna, get fat")

    # dun dun, dun dun dund udn dun dun dun, dun dun dun, dom dom
    if message.content == command_prefix + "imposter":
      message.channel.send(file=discord.File('images/sussychung.png'))

    # big big chungus, big chungus, big chungus
    if message.content == command_prefix + "chungus":
      message.channel.send(file=discord.File('images/chung.png'))

    # I know it was you, I saw you do it
    if message.content == command_prefix + "isawyoudoit":
      message.channel.send(file=discord.File('images/see you.jpg'))

    # When the imposter is sus
    if message.content == command_prefix + "jerma":
      message.channel.send(file=discord.File('jerma/sussy.png'))

    # OMG GUYS FACE REVEAL?!??!?!?!?!1?
    if message.content == command_prefix + "door":
      message.channel.send("face reveal!!!")
      message.channel.send(file=discord.File('images/a hecking door.jpg'))

    ## Message commands
    # Go subscribe right now
    if message.content == command_prefix + "youtube":
        message.channel.send("https://www.youtube.com/channel/UCK1VJI8Gyh6qfozmqezTHsg")

    # PFOFOOBFBOBFBT
    if message.content == command_prefix + "fard":
        message.channel.send("\*fard sound effect\*")

    # No seriously call the ambulance
    if message.content == command_prefix + "help":
        message.channel.send("no")

    # why do you want Gex to die?
    if message.content == command_prefix + "die":
        message.channel.send("uno reverse card")