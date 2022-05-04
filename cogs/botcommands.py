import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import config
import random
import wikipedia

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
        embed = discord.Embed(title='BoardGameBot', colour=discord.Colour.random(),
                              description='BoardGameBot is a multipurpose Discord bot with board games. Read more at https://github.com/WhiteWolfSV/BoardGameBot')
        embed.set_image(url='https://upload.wikimedia.org/wikipedia/en/8/87/Keyboard_cat.jpg')
        await ctx.author.send(embed=embed)
        await ctx.send('DM sent!')

    @commands.command()
    async def members(self, ctx):
        onlineMembers = [member.name for member in ctx.guild.members]
        embed = discord.Embed(title=f'Members in {ctx.guild}', colour=discord.Colour.dark_red(), description='\n'.join(onlineMembers))
        await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx, *, wiki):
        try:
            page = wikipedia.page(wiki, auto_suggest=False, redirect=True, preload=False)
            sum = wikipedia.summary(page.title, sentences=2)
            embed = discord.Embed(title=page.title, url=page.url, description=sum)
            await ctx.send(embed=embed)
        except wikipedia.DisambiguationError as e:
            page = wikipedia.page(e.options[0], auto_suggest=False, redirect=True, preload=False)
            sum = wikipedia.summary(page.title, sentences=2)
            embed = discord.Embed(title=page.title, url=page.url, description=sum)
            await ctx.send(embed=embed)

        '''async with aiohttp.ClientSession() as session:
            async with session.get(wiki) as r:
                if r.status == 200:
                    await ctx.send('Wikipedia entry exists.')
                else:
                    await ctx.send('Wikipedia entry does not exist!')
'''
async def setup(bot):
    await bot.add_cog(BotCommands(bot))
