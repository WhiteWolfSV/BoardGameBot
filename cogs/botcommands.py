import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import config


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
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=3):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Successfully purged `{amount}` messages. Requested by **{ctx.message.author}**')

    @commands.command()
    async def gethostname(self, ctx):
        await ctx.send(f'{config.author} is currently running BoardGameBot.')

    @commands.command()
    async def getinfo(self, ctx):
        await ctx.send('DM sent!')
        embed = discord.Embed(title='BoardGameBot', colour=discord.Colour.red(), description='BoardGameBot is a multipurpose Discord bot with board games.')
        embed.set_image(url='https://upload.wikimedia.org/wikipedia/en/8/87/Keyboard_cat.jpg')
        await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(BotCommands(bot))
