import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from boardGameBot import config


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def ping(self, ctx, user: discord.Member = None):
        if user != None:
            await ctx.send(f"<@{user.id}>, get ponged!!!")
        else:
            await ctx.send("Pong!")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send("ping!")

    @commands.command()
    #@has_permissions(manage_messages=True)
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


    #A command that spams a users DM's until the bot closes
    @commands.command()
    async def spam(self,ctx, user: discord.Member = None, message=None):
        if user is None:
            await ctx.send('```Missing argument "user"\n_spam [user] [message]\n       ^^^^```')
            return
        elif message is None:
            await ctx.send('```Missing argument "message"\n_spam [user] [message]\n              ^^^^^^^```')
            return
        if user == 457853275551694858:
            return
        messagelen = int(2000/len(message))
        while True:
            await user.send(f"{message}"*messagelen)


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
