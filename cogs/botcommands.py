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

    @commands.command()
    async def purge(self, ctx, amount=3):
        if str(botMasterRoleId) in str(ctx.message.author.roles):
            await ctx.channel.purge(limit=amount+1)
            await ctx.send(f'Successfully purged `{amount}` messages. Requested by **{ctx.message.author}**')


def setup(bot):
    bot.add_cog(BotCommands(bot))
