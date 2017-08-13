import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("Ready for commands...")

#adds two numbers
@client.command()
async def add(a: int, b: int):
    """Adds two numbers together"""
    await client.say(a + b)

#greets user
@client.event
async def on_message(message):
    #prevents the bot from replying to itself
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    await client.process_commands(message)

#creates a poll
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$poll"):
        rcts = ["\U0001F44D", "\U0001F44E", "\U0001F937"]
        i = 0
        while i < len(rcts):
            await client.add_reaction(message, rcts[i])
            i += 1

    await client.process_commands(message)

client.run("MzQzNDg1NTYwMzk0MDg4NDQ4.DGfT1Q.LZY3VSwPPG3x_jNYfFQ5178kmVE")
