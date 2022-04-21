import numpy
from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttt(self, ctx):
        w, h = 3, 3
        b = [["  " for x in range(w)] for y in range(h)]

        winner = 'none'
        player1 = 'X'
        player2 = 'O'
        curentplayer = player1
        nextplayer = player2

        Run = True
        def printboard(b):
            await ctx.send(f"|{b[0][0]}|{b[0][1]}|{b[0][2]}|"
                           f"\n------------------------"
                           f"\n|{b[1][0]}|{b[1][1]}|{b[1][2]}|"
                           f"\n------------------------"
                           f"|{b[1][0]}|{b[1][1]}|{b[1][2]}|\n")
        printboard(b)

        def fill(b):
            await ctx.send(f"fill in box")
            inpx = await ctx.send("row: ")
            inpy = await ctx.send("column: ")

            if inpx >= 1 and inpx <= 2 and b[inpx] != nextplayer:
                if inpy >= 1 and inpx <=2 and b[inpy] != nextplayer:
                    b[inpx][inpy] = [curentplayer][curentplayer]



        curentPlayer = player1

        await ctx.send(f"Player ones turn. comment _help for help to play")



    async def help(self, ctx):
        await ctx.send(f"to fill a box press x(column), y(row)")
        await ctx.send(f"for instance: 2, 2 for center")