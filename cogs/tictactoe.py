import numpy
from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttt(self, ctx):
        # Here it prints out the numbers
        w, h = 8, 5
        b = [["  " for x in range(w)] for y in range(h)]
        await ctx.send(f"|{b[1][1]}|{b[2][1]}|{b[3][1]}|") # Row 1
        await ctx.send(f"|{b[1][2]}|{b[2][2]}|{b[3][2]}|") # Row 2
        await ctx.send(f"|{b[1][3]}|{b[2][3]}|{b[3][3]}|") # Row 3