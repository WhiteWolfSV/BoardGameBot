from discord.ext import commands


class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ttt(self, ctx):
        w, h = 8, 5
        b = [["  " for x in range(w)] for y in range(h)]
        await ctx.send(f"|{b[0][0]}|{b[1][0]}|{b[2][0]}|")


def setup(bot):
    bot.add_cog(TicTacToe(bot))
