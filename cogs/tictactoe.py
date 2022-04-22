import numpy
from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttt(self, ctx):
        w, h = 3, 3
        b = [["  " for x in range(w)] for y in range(h)]

        winner = 'none' # Settings for the game
        player1 = 'X'
        player2 = 'O'
        curentplayer = player1
        nextplayer = player2

        Run = True
        def printboard(b): # Print the board
            await ctx.send(f"|{b[0][0]}|{b[0][1]}|{b[0][2]}|"
                           f"\n------------------------"
                           f"\n|{b[1][0]}|{b[1][1]}|{b[1][2]}|"
                           f"\n------------------------"
                           f"|{b[1][0]}|{b[1][1]}|{b[1][2]}|\n")
        def fill(b): # Conditions when it comes to filling the boards
            retry = True
            while retry == True:
                await ctx.send(f"fill in box")
                inpx = await ctx.send("row: ")
                inpy = await ctx.send("column: ")
                if inpx >= 1 and inpx <= 2 and b[inpx] == " ":
                    if inpy >= 1 and inpx <= 2 and b[inpy] == " ":
                        b[inpx][inpy] = [curentplayer][curentplayer]
                        retry = False
                    else:
                        await ctx.send("Faulty input. Try again!")
                await ctx.send("Faulty input. Try again!")

        def CheckColumn(b): # Chekcs by column
            global winner
            if b[0][0] == b[0][1] == b[0][2] and b[0][1] != " ":
                winner == b[0][0]
                return True

            elif b[1][0] == b[1][1] == b[1][2] and b[1][1] != " ":
                winner == b[1][0]
                return True
            elif b[2][0] == b[2][1] == b[2][2] and b[2][1] != " ":
                winner == b[2][0]
                return True

        def CheckRow(b): # Chekcs by Row
            global winner
            if b[0][0] == b[1][0] == b[2][0] and b[1][0] != " ":
                winner == b[0][0]
                return True

            elif b[0][1] == b[1][1] == b[2][1] and b[1][1] != " ":
                winner == b[1][0]
                return True
            elif b[0][2] == b[1][2] == b[2][2] and b[1][2] != " ":
                winner == b[1][0]
                return True
        def CheckDiag(b): # Chekcs by Diagonal
            global winner
            if b[0][0] == b[1][1] == b[2][2] and b[1][1] != " ":
                winner == b[0][0]
                return True

            elif b[0][2] == b[1][1] == b[2][0] and b[1][1] != " ":
                winner == b[1][0]
                return True
        def ChekcTie(b): #Check for ties
            global again
            if "" not in b:
                printboard(b)
                await ctx.send("Tie")
                again = False

        def Win(b):
            if CheckDiag(b) or CheckRow(b) or CheckColumn():
                ctx.send(f"Winner is{winner}")
                again = False

        def switchplayer():
            global curentplayer
            if curentplayer == player1:
                curentplayer = player2
                nextplayer = player1
            elif curentplayer == player2:
                curentplayer = player1
                nextplayer = player2
        while again:
            printboard(b)
            fill(b)
            Win()
            ChekcTie(b)
            switchplayer()

