import discord
from discord.ext import commands
import random

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    global b
    w, h = 3, 3

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
        global count
        curentplayer = " "
        count = 0
        gameend = True
        if gameend:
            WinConditions = [0, 1, 2], \
                            [3, 4, 5], \
                            [6, 7, 8], \
                            [0, 3, 6], \
                            [1, 4, 7], \
                            [2, 5, 8], \
                            [0, 4, 8], \
                            [2, 4, 6]

            global brd
            brd = ["T", "T", "T", # Board format
                   "T", "T", "T",
                   "T", "T", "T"]
            gameend = False
            player1 = p1
            player2 = p2

            # Print out the board
            line = ""
            for x in range(len(brd)): # Print out a board
                if x == 2 or x == 5 or x == 8:
                    line += " " + brd[x]
                    await ctx.send(line)
                    line = ""
                else:
                    line += " " + brd[x]

            num = random.randint(1, 3) #Randomly generates a number between 1 and 2 to decide who starts
            if num == 1:
                curentplayer = player1
            elif num == 2:
                curentplayer = player2
            await ctx.send("* <@" + str(curentplayer.id) + "> Starts!")

        else:
            await ctx.send("Game is running")
    @commands.command()
    async def fill(self, ctx, inp: int): #Fill comand
        global player1
        global player2
        global brd
        global turn
        global gameend
        global curentplayer
        global b
        global mark
        global count

        if gameend == False:
            if curentplayer == ctx.author: #if it's the turn of the one using this comand
                if curentplayer == player1:
                    mark = "X"
                else:
                    mark = "O"
                if 0 < inp < 10 and brd[inp - 1] == "T": #check if everything goes
                         brd[inp - 1] = mark
                         count = count + 1
                         line = " "
                         for x in range(len(brd)): # Print out the board again
                             if x == 2 or x == 5 or x == 8:
                                 line += " " + brd[x]
                                 await ctx.send(line)
                                 line = " "
                             else:
                                 line += " " + brd[x]
                else:
                    await ctx.send("Faulty input. Please try again(Use int between 1 and 9)")
                    await ctx.send(brd)
            else:
                await ctx.send("Please wait until it's your turn")
                await ctx.send(brd)
        else:
            await ctx.send("Start a new game to use this command")
            await ctx.send(brd)

        if count == 9:
            await ctx.send("It's a tie!")
            gameend = True


        def win(WinConditions, mark): #Checks if win conditions are fufilled
            for conditions in WinConditions:
                if brd[conditions[0]] == mark and brd[conditions[1]] == mark and brd[conditions[2]] == mark:
                    gameend = True
                    return gameend

        win(WinConditions, mark) #Prints out the winner
        if gameend == True:
            await ctx.send("Winner: ", curentplayer)

        if curentplayer == player1: # Switches player
            curentplayer = player2
        elif curentplayer == player2:
            curentplayer = player1


async def setup(bot):
    await bot.add_cog(TicTacToe(bot))
