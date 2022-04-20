from discord.ext import commands
import botToken
from discordBot.cogs.tictactoe import TicTacToe

bot = commands.Bot(command_prefix="_")


@bot.event
async def on_ready():
    print('We successfully logged in as {0.user}'.format(bot))
bot.add_cog(TicTacToe(bot))


@bot.command()
async def cog_reload(ctx):
    bot.remove_cog("TicTacToe")
    bot.add_cog(TicTacToe(bot))
    await ctx.send("Reloaded tictactoe.")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


@bot.command()
async def pong(ctx):
    await ctx.send("ping!")


@bot.command()
async def stop(ctx):
    await ctx.send("Stopping all processes...")
    await bot.close()

if __name__ == '__main__':
    bot.run(botToken.botToken)