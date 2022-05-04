import discord
from discord.ext import commands
import json
import random

class cog_extentions(commands.Cog):
    def __init__(self,bot):
        self.bot = bot