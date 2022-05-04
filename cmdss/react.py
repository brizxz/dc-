import discord
from discord.ext import commands
import json
import random
from core.classes import cog_extentions
with open("C:\\Users\\User\\Desktop\\成果\\dc機器人\\.vscode\\setting.json", mode="r",encoding="utf-8") as file:
   jdata=json.load(file)
class react(cog_extentions):

    @commands.command()
    async def 圖(self,ctx):
        picpic=random.choice(jdata["pic"])
        pic=discord.File(picpic)
        await ctx.send(file=pic)
    @commands.command()
    async def 桐人(self,ctx):
        pic=jdata["urlpic"]#是一個網址，所以直接送出
        await ctx.send(pic)
def setup(bot):
    bot.add_cog(react(bot))