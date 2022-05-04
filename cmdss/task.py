import discord
from discord.ext import commands
import json
from datetime import *
import random,asyncio
from core.classes import cog_extentions
with open("C:\\Users\\User\\Desktop\\成果\\dc機器人\\.vscode\\setting.json", mode="r",encoding="utf-8") as file:
   jdata=json.load(file)
class Task(cog_extentions):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #父類別的初始化設定(self.bot=bot
        #不是原本的功能故不用裝飾器
        self.counter=0
        """
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(938063417783230464)
            while not self.bot.is_closed():
                await self.channel.send("that is okay") #自動執行，故無ctx
                await asyncio.sleep(10) #5秒
            
            
        self.bg_task= self.bot.loop.create_task(interval())
        """                
        async def timetask():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(971048754041991218)
            while not self.bot.is_closed():
                now_time=datetime.now().strftime("%H%M")
                if now_time==jdata["time"] and self.counter==0:
                    await self.channel.send("Task working")
                    self.counter=1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        self.bg_task= self.bot.loop.create_task(timetask())
    @commands.command()
    async def set_channel(self,ctx,cha:int): 
        self.channel =self.bot.get_channel(cha) #設置成別的頻道
        await ctx.send(f"set channel:{self.channel.mention}")
     
    @commands.command()
    async def set_time(self,ctx,time):
        self.counter=0
        jdata["time"]= time
        with open("setting.json","w",encoding="utf-8") as file:
            json.dump(jdata,file, indent=4) #indent:縮排

def setup(bot):
    bot.add_cog(Task(bot))