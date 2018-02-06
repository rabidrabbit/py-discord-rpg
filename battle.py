import discord
from discord.ext import commands

class BattleSystem():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def attack(monsterNum : int):

def setup(bot):
    bot.add_cog(BattleSystem(bot))
