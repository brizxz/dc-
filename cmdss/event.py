from ast import keyword
import discord
from discord.ext import commands
import json
import random
from core.classes import cog_extentions
with open("C:\\Users\\User\\Desktop\\成果\\dc機器人\\.vscode\\setting.json", mode="r",encoding="utf-8") as file:
   jdata=json.load(file)
class event(cog_extentions):
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel= self.bot.get_channel(int(jdata["welcome"])) #抓取頻道
        await channel.send(f"{member} join welcome!") #用f字串因成員名字為變數

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel=self.bot.get_channel(int(jdata["leave"])) #抓取頻道
        await channel.send(f"{member} leave so sad")

    @commands.Cog.listener() #一個機器人只有一個 on_message
    async def on_message(self,msg):
        if msg.content.endswith("媽") or msg.content in jdata["banned words"] and msg.author!=self.bot: #防止無限啟動
            await msg.channel.send("尊重一點")
    
#處理指令發生的錯誤 error handler 公用的
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        #檢查指令是否有自己的error handler:如果有就跳過
        if hasattr(ctx.command,"on_error"):
            return
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("遺失參數") 
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("無此指令")
        else:
            await ctx.send("error") #了解錯誤
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload): #raw是從discord抓的
        #新增反應貼圖獲得身分組
        #判斷反應的訊息是否為指定的訊息
        if payload.message_id == 971387417300987924:
            if str(payload.emoji)=="😕":
                guild = self.bot.get_guild(payload.guild_id)
                role=guild.get_role(971382244478447708) #guild為當前伺服器
                await payload.member.add_roles(role) #coroutine為協成功能
                await payload.member.send(f"你獲得了{role}身分組")
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload): 
      #  if payload.message_id == 971387417300987924:
        if str(payload.emoji)=="😕":
            guild = self.bot.get_guild(payload.guild_id)
            user = guild.get_member(payload.user_id)
            role=guild.get_role(971382244478447708) 
            await user.remove_roles(role)
            await user.send(f"你的 {role} 被移除ㄌ") 
    @commands.Cog.listener()
    async def on_message_delete(self,msg):
        counter=1
        async for entry in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
            if counter==1:
                await msg.channel.send("刪除的人"+str(entry.user.name))
                counter+=1
        await msg.channel.send("訊息刪除內容"+str(msg.content))
        await msg.channel.send("訊息原本的作者"+str(msg.author))
       
def setup(bot):
    bot.add_cog(event(bot))       