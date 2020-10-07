import discord
from discord.ext import commands
import random
from discord import Game
TOKEN = 'NzMwMzU0MjY4MzE3NTQ4NTY0.XwWV5g.stoKK_ueDq9TPnqnEiUdeQM61JQ'


BOT_PREFIX = ("?", "!")
client = commands.Bot(command_prefix=BOT_PREFIX,case_insensitive=True)

#confirmation that bot is ready
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



@client.command()
async def ping(ctx):   #ctx is context that must be passed as a first argument
    await ctx.send(f'pong!{round(client.latency*(1000))}ms')


@client.command(name="hello",aliases=["hi","hii","helloo","hey"])
async def hello(ctx):
    reply = ["hi","hii","helloo",]
    msg = f'{random.choice(reply)} {ctx.message.author.mention}'
    await ctx.send(msg)


#modifying help command to give the list of available commands
#to modify first delete the default existing command
client.remove_command('help')
#program to modify
@client.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(colour=discord.Colour.green())
    embed.set_author(name='help:Here is the list of commands available')
    embed.set_field(name='!hello',value='greets you',inline=False )
    embed.add_field(name='!ping',value='shows latency',inline=False)
    embed.set_field(name='!dm',value='messages you personally ',inline=False )
    await ctx.send(embed=embed)


#program that makes the bot to message u privately by command 
@client.command()
async def dm(ctx):
    await ctx.author.send("hello")

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

client.run(TOKEN)
