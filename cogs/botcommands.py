from discord.ext import commands
import discord

from boardGameBot.main import botMasterRoleId


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send("ping!")


def setup(bot):
    bot.add_cog(BotCommands(bot))
