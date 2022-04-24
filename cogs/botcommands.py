from discord.ext import commands
from discord.ext.commands import has_permissions
import socket
import discord


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
        localip = socket.gethostbyname(socket.gethostname())
        user_to_ip = {'10.153.222.48': 'Theodors dator', '192.168.10.209': 'Pauls dator'}  # Use a dictionary in order
        # to avoid
        # repetitive and ambiguous code. Format IP: HOSTNAME
        for i in user_to_ip:
            if i == localip:
                await ctx.send(f'{user_to_ip[i]}: {i}')

def setup(bot):
    bot.add_cog(BotCommands(bot))
