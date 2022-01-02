# import the installs
import nextcord
import random # you may need to do pip install random in a terminal
from nextcord.ext import commands

intents = nextcord.Intents.all()
# also  we need to enable intents in dev portal
# that easy!!

# this defines the client
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    # this outputs Bot ready! when connected to discord
    print("Bot ready!")


@client.command()
async def ping(ctx):
    # this sends a message to the channel
    await ctx.send(f"Pong! Bot latency = {round(client.latency * 1000)}ms.") # we have the bots latency now when we enter the command. lets test



    # currently the bot only says Pong!. but what if we added the latency?
  


# welcome back: part 2
# -----------------------------

# today we will be improving the ping command and adding an 8ball command


# since we cannot make the name 8ball we shall add an alias, this adds a 2nd name to use the commands.

@client.command(aliases=["8ball", "eight-ball", "8-ball"]) # you can add as many as you want.
async def eightball(ctx, *, question):
    # we need to define the question so that the user can ask a question for bot to answer.
    # the * makes it so we can enter more than 1 word in the question
    # we need some responses for the bot so lets go onto google chrome to find some responses

    responses = [
        
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",

        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",

        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",

        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    # we can use the reply feature of ctx; this replies to user instead of just sending in to channel.
    # to use the 8ball command we need a libary called random. this gets a bunch of info and randomizes it to 1 left.
    await ctx.reply("Your question is: " + question + "\nMy answer: " + random.choice(responses))






# part 3 ----------------------------------------------
# welcome back to part 3. today we will be creating and learning about events and how to use them in a discord bot.
# we shall make an event where someone joins and prints a message and sends a message to a channel...
# lets go!
# to do this we need something called intents.... lets go into discord dev portal, we now need to define them in the bot code

@client.event
async def on_member_join(member):
    print(member.name + " has joined a server!!") # this is a basic event like on_ready... lets test! oops we need Intents not intents 
    await client.get_channel(926990486516949002).send(member.name + " has joined a server!!!")





















# control + c = stop bot


# this runs the client and connects to discord
client.run("OTI2OTUwNzA0NDAzMzM3MjI3.YdDIHQ.DTYgnucS5oC5PWvoReswAOLQx9E") 
