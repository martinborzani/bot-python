import discord
from discord import embeds
from discord.colour import Color
from discord.ext import commands
import datetime
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='!', description="this is a helper bot")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numone: int, numtwo: int):
 await ctx.send(numone + numtwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description= "claro que si", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name= "Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name = "Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server id", value=f"{ctx.guild.id}")
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
   queary_string = parse.urlencode({'search_query': search}) 
   html_content = request.urlopen('http://www.youtube.com/results?' + queary_string)
   search_result = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
   print(search_result)
   await ctx.send('https://www.youtube.com/watch?v=' + search_result[0])


@bot.command()
async def happy(ctx, user):
    await ctx.send('Feliz cumpleaños culo roto ' + user) 

 # Events

@bot.event
async def on_ready():
     await bot.change_presence(activity=discord.Streaming(name='Tutorials', url="https://www.twitch.tv/rainbow6latam"))
     print('My bot is ready')     
    

bot.run('ODQzOTkyNjc2NTkxMjA2NDAw.YKL7bg.-RBSocMm0noHKYARdU04uUSRJ0k')