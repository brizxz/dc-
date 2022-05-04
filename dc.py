import random
import discord
import json
from discord.ext import commands
import os
with open("C:\\Users\\User\\Desktop\\成果\\dc機器人\\.vscode\\setting.json", mode="r",encoding="utf-8") as file:
   jdata=json.load(file) 

intents=discord.Intents.all()
intents.members=True
#指揮機器人
bot= commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmdss.{extension}')
    await ctx.send(f'loaded {extension} done ')
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmdss.{extension}')
    await ctx.send(f'unloaded {extension} done ')
@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmdss.{extension}')
    await ctx.send(f'reloaded {extension} done ')
 
for filename in os.listdir("./cmdss"):
    if filename.endswith(".py"):
        bot.load_extension(f'cmdss.{filename[:-3]}')

if __name__ == "__main__":
    pass

bot.run(jdata["TOKEN"])    

    