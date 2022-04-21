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

        winner = 'none'
        player1 = 'X'
        player2 = 'O'
        Run = True

        await ctx.send(f"|{b[1][1]}|{b[2][1]}|{b[3][1]}|") # Row 1
        await ctx.send("------------------------")
        await ctx.send(f"|{b[1][2]}|{b[2][2]}|{b[3][2]}|") # Row 2
        await ctx.send("------------------------")
        await ctx.send(f"|{b[1][3]}|{b[2][3]}|{b[3][3]}|") # Row 3

        curentPlayer = player1

        await ctx.send(f"Player ones turn. comment _help for help to play")

    async def help(self, ctx):
        await ctx.send(f"to fill a box press x(column), y(row)")
        await ctx.send(f"for instance: 2, 2 for center")