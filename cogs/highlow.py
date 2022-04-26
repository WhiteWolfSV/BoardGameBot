import discord
from discord.ui import Button
from discord.ext import commands


class HighLow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hl(self, ctx):
        button = Button(style=discord.ButtonStyle.green)
        await ctx.send("Test", components=[button])


async def setup(bot):
    await bot.add_cog(HighLow(bot))
