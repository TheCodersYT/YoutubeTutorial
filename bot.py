# import the installs
import nextcord
from nextcord.ext import commands

# this defines the client
client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    # this outputs Bot ready! when connected to discord
    print("Bot ready!")


@client.command()
async def ping(ctx):
    # this sends a message to the channel
    await ctx.send("Pong!")



# control + c = stop bot


# this runs the client and connects to discord
client.run("OTI2OTUwNzA0NDAzMzM3MjI3.YdDIHQ.eEaQbMx0I6e9vWS0CnNtlleyIhg") 
