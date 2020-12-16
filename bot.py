import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    #confirms bot is running
    print("Bot is ready to use.")

@client.command()
async def ping(ctx):
    #test to see if the bot works
    await ctx.send(f"{ctx.author.mention} Hello, you pinged me.")

@client.command()
async def bonk(ctx, user1: discord.Member):
    await ctx.send(f"{ctx.author.mention} has bonked {user1.mention}.")


client.run(token)