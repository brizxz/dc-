from datetime import *
from click import command
#async 異部執行
import discord
from discord.ext import commands
import json
import random
from core.classes import cog_extentions
with open("C:\\Users\\User\\Desktop\\成果\\dc機器人\\.vscode\\setting.json", mode="r",encoding="utf-8") as file:
   jdata=json.load(file) 
class main(cog_extentions):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx): #ctx=context 上下文
        await ctx.send(f'{round(self.bot.latency*1000)} ms')
    @commands.command()
    async def hi(self,ctx): #ctx=context 上下文
        await ctx.send("hi")
    @commands.command()
    async def randice(self,ctx): #ctx=context 上下文
        a=random.choice(1,6)
        await ctx.send(a)
    timestamp=datetime.now()
    @commands.command()
    async def embed(self,ctx): 
        embed=discord.Embed(title="briz", url="https://www.cpbl.com.tw/", description="introduction", color=0x3cc5d7, 
        timestamp=datetime.utcnow()) #使用utcnow就變台灣時間?
        embed.set_author(name="briz", url="https://www.facebook.com/profile.php?id=100015259690780", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQHxYb09GEAQRehd20YsiyrlD3XJwKRbo8iZQ&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS803TbLNXtzEvhfWjJnwFtsOrgmhK-VMaWA&usqp=CAU")
        embed.add_field(name="1", value="青青子衿 悠悠我心", inline=True)
        embed.add_field(name="2", value="十秒十六劍", inline=True)
        embed.add_field(name="3", value="it ain`t over till it is over", inline=True)
        embed.add_field(name="4", value="最美不過下雨天", inline=True)
        await ctx.send(embed=embed)
    @commands.command()
    async def sayagain(self,ctx,*,msg): #星號後所有皆做為msg，不論空格
       await ctx.message.delete()
       await ctx.send(msg) 
    @commands.command()
    async def 刪除(self,ctx,num : int): #num可直接做為整數型態
        await ctx.channel.purge(limit=num)
    @commands.command()
    async def ran_squad(self,ctx):  #隨機分組
        online=[]
        for member in ctx.guild.members:
            if str(member.status) == "online" and member.bot == False :
                online.append(member.name)
        random_online=random.sample(online,k=20) #k為指定，sample不同於choices，它不會重複
        for i in range(1,5):
            random_sample=random.sample(random_online, k=5)
            await ctx.send(f"第{i}小隊"+ str(random_sample))
            for name in random_sample:
                random_online.remove(name)       
    @commands.command()
    async def cmda(self,ctx,num):
        await ctx.send(num)
    #指令個別專用的錯誤處理
    @cmda.error
    async def cmda_error(self,ctx,error):
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("請輸入參數") 
"""   不推薦因try except 每行都要寫         
    @commands.command()
    async def cmdc(self,ctx,num:str):
        try: #python內建的判斷
            await ctx.send(num)
        except Exception as e:
            await ctx.send("錯誤") """

def setup(bot):
    bot.add_cog(main(bot))