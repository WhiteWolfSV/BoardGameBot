from discord.ext import commands
import botToken
import discord
import os

bot = commands.Bot(command_prefix="_")


@bot.event
async def on_ready():
    print('We successfully logged in as {0.user}'.format(bot))


bot.load_extension('cogs.tictactoe')


# Added a way to reload cogs.
@bot.command()
async def cog_reload(ctx, cogname):
    if "966332497862484068" in str(ctx.message.author.roles):
        try:
            bot.unload_extension(f"cogs.{cogname}")
            bot.load_extension(f"cogs.{cogname}")
            await ctx.send(f"Successfully Reloaded {cogname}.")
        except:
            await ctx.send("Couldn't find the specified cog you were looking for.")
    else:
        await ctx.send("You dont have the required role to access this command.")


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
