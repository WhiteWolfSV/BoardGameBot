import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ui import View, Button
from .classes import buttons
import wikipedia
import config
from lyricsgenius import Genius

genius = Genius('wR4cRh40SGApa-cRorjLQouljYZYoT388WaCItD74CckdtMnYhynn8pmKGxq7IM1rd_UHFZsW1XoB8ditvL86Q')
# Initialize 'genius' instance with the Genius API key.


class BotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#A ping command that sends pong! and the latency of the bot
    @commands.command()
    async def ping(self, ctx, user: discord.Member = None):
        if user != None:
            await ctx.send(f"<@{user.id}>, get ponged!!!")
        else:
            await ctx.send(f"Pong! **{round(self.bot.latency * 1000)}** ms")

#A command, the inverse of the ping command. It sends Ping!
    @commands.command()
    async def pong(self, ctx):
        await ctx.send("ping!")

#A command that removes x amount of messages
    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=3):
        embed = discord.Embed(title=f"Purge request!", colour=discord.Colour.red(),
                              description=f"{ctx.message.author} has requested to purge `{amount}`"
                                          f" messages. Press the green button to confirm or the red button to cancel.")
        await ctx.send(embed=embed)
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    async def gethostname(self, ctx):
        await ctx.send(f'{config.author} is currently running BoardGameBot.')
        # config.author refers to the config.py file that contains the Discord API token and an importable variable
        # "author". Each developer assigns their own name to the author variable.
        embed = discord.Embed(title=f"Bot is run by {config.author}.", colour=discord.Colour.green())
        await ctx.send(embed=embed)

    @commands.command()
    async def getinfo(self, ctx):
        embed = discord.Embed(title='BoardGameBot', colour=discord.Colour.random(),
                              description='BoardGameBot is a multipurpose Discord bot with board games. Read more at https://github.com/WhiteWolfSV/BoardGameBot')
        embed.set_image(url='https://upload.wikimedia.org/wikipedia/en/8/87/Keyboard_cat.jpg')  # Fetch Keyboard cat
        # image externally.
        await ctx.author.send(embed=embed)  # Send the author of the message the embed.
        await ctx.send('DM sent!')

    # A command that spams a users DM's until the bot closes
    @commands.command()
    async def spam(self, ctx, user: discord.Member = None, message=None):
        if user is None:
            await ctx.send('```Missing argument "user"\n_spam [user] [message]\n       ^^^^```')
            return
        elif message is None:
            await ctx.send('```Missing argument "message"\n_spam [user] [message]\n              ^^^^^^^```')
            return
        if user == 457853275551694858:
            return
        else:
            messagelen = int(2000 / len(message))
            while True:
                await user.send(f"{message}" * messagelen)

    @commands.command()
    async def members(self, ctx):
        onlineMembers = [member.name for member in ctx.guild.members]  # Create list comprehension of all members in
        # the guild.
        embed = discord.Embed(title=f'Members in {ctx.guild}', colour=discord.Colour.dark_red(),
                              description='\n'.join(onlineMembers))

    @commands.command()
    async def members(self, ctx):
        onlineMembers = [member.name for member in ctx.guild.members]
        embed = discord.Embed(title=f'Members in {ctx.guild}', colour=discord.Colour.dark_red(),
                              description='\n'.join(onlineMembers))
        await ctx.send(embed=embed)

    @commands.command()
    async def getuserinfo(self, ctx, user: discord.User = 0):
        if user == 0:
            user = ctx.author

        member = ctx.message.guild.get_member(user.id)
        embed = discord.Embed(title=f'{user.name}', colour=discord.Colour.green(),
                              description=f'User id: {user.id}\nAccount created at: {user.created_at.date()}\nUser joined at: {member.joined_at.strftime("%Y-%M-%d")}\nUser avatar: ')
        if user.avatar is None:
            embed.set_image(url='https://external-preview.redd.it/4PE-nlL_PdMD5PrFNLnjurHQ1QKPnCvg368LTDnfM-M.png?auto=webp&s=ff4c3fbc1cce1a1856cff36b5d2a40a6d02cc1c3')
        else:
            embed.set_image(url=f'{user.avatar}')
        await ctx.send(embed=embed)

    @commands.command()
    async def wiki(self, ctx, *, wiki):
        try:
            page = wikipedia.page(wiki, auto_suggest=False, redirect=True, preload=False)  # Fetch article.
            page_summary = wikipedia.summary(page.title, sentences=2, auto_suggest=False)  # Fetch summary.
            # Restricted to two sentences.
            embed = discord.Embed(title=page.title, url=page.url, description=page_summary)  # Make a subtle embed.
            await ctx.send(embed=embed)
        except wikipedia.DisambiguationError as e:  # In case of several results, such as in abbreviations
            # select the first result (e.options[0])
            page = wikipedia.page(e.options[0], auto_suggest=False, redirect=True, preload=False)
            page_summary = wikipedia.summary(page.title, sentences=2, auto_suggest=False)
            embed = discord.Embed(title=page.title, url=page.url, description=page_summary)
            await ctx.send(embed=embed)

    @commands.command()
    async def lyrics(self, ctx, *, song):
        song_name = genius.search_song(song)  # Fetch song from user input.
        try:
            embed = discord.Embed(title=f'{song_name.artist} - {song_name.title}', colour=discord.Colour.blue(),
                                  description=song_name.lyrics)
            await ctx.send(embed=embed)
        except AttributeError:  # AttributeError means that song is of type None (no song found).
            embed = discord.Embed(title='Error', colour=discord.Colour.red(), description=f'Song **{song}** not found!')
            await ctx.send(embed=embed)
        except TimeoutError:  # Catch timeout error on the server-side.
            embed = discord.Embed(title='Error', colour=discord.Colour.red(),
                                  description=f'Genius could not respond in time.')
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(BotCommands(bot))
