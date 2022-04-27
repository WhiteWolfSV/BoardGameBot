import discord
import numpy
from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttt(self, ctx, p1: discord.Member, p2: discord.Member):
        # Settings for the game
        global WinConditions
        global player1
        global player2
        global gameend
        global turn
        global curentplayer
        global brd
        global b
        player1 =p1
        player2 = p2
        curentplayer = player1
        gameend = True


        if gameend:
            w, h = 3, 3
            b = [["Empty" for x in range(w)] for y in range(h)]
            WinConditions = [b[0][0], b[0][1], b[0][2]], \
                            [b[1][0], b[1][1], b[1][2]], \
                            [b[2][0], b[2][1], b[2][2]], \
                            [b[0][0], b[1][0], b[2][0]], \
                            [b[0][1], b[1][1], b[2][1]], \
                            [b[0][2], b[1][2], b[2][2]], \
                            [b[0][0], b[1][1], b[2][2]], \
                            [b[0][2], b[1][1], b[2][0]]
            global brd
            brd = (f"|{b[0][0]}|{b[0][1]}|{b[0][2]}|"
                   f"\n---------------"
                   f"\n|{b[1][0]}|{b[1][1]}|{b[1][2]}|"
                   f"\n---------------"
                   f"|{b[2][0]}|{b[2][1]}|{b[2][2]}|\n")
            await ctx.send(brd) #Print out the board
            gameend = False
        else:
            await ctx.send("Game is running")
    @commands.command()
    async def fill(self, ctx, inpx: int, inpy: int):
        global player1
        global player2
        global brd
        global turn
        global gameend
        global curentplayer
        global b

        if gameend == False:
            if curentplayer == ctx.author: #if it's the turn of the one using this comand
                if curentplayer == player1:
                    mark = "X"
                else:
                    mark = "O"
                if -1 < inpx < 3: #check if everything goes
                    if -1 < inpy < 3:
                        b[inpx][inpy] = mark #Problem with fill
                        await ctx.send(brd)

                    else:
                        await ctx.send("Faulty input. Please try again(Use int between 0 and 2 for x and y)")
                        await ctx.send(brd)
                else:
                    await ctx.send("Faulty input. Please try again(Use int between 0 and 2 for x and y)")
                    await ctx.send(brd)
            else:
                await ctx.send("Please wait until it's your turn")
                await ctx.send(brd)
        else:
            await ctx.send("Start a new game to use this command")
            await ctx.send(brd)

        if "" not in brd:
            await ctx.send("Tie") #Check if it's a tie
            gameend = True


        def win(WinConditions, mark): #Checks if win conditions are fufilled
            for conditions in WinConditions:
                if brd[0] == mark and brd[1] == mark and brd[2] == mark:
                    Gameend = True

        win(WinConditions, mark)
        if gameend == True:
            await ctx.send("Winner is: ", curentplayer)

        if curentplayer == player1: #Switches player
            curentplayer = player2
        elif curentplayer == player2:
            curentplayer = player1

    @commands.command()
    async def tictactoe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("please mention 2 players for this comand")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make shure to mention players using @")


def setup(bot):
    bot.add_cog(TicTacToe(bot))