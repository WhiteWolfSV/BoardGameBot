from discord.ext import commands
import botToken
import discord
import os

bot = commands.Bot(command_prefix="_")


@bot.event
async def on_ready():
    print('We successfully logged in as {0.user}'.format(bot))


bot.load_extension('cogs.tictactoe')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(f"Missing arguments: `{error}`")
    else:
        await ctx.send(error)


# Added a way to reload cogs.
@bot.group()
async def cog(ctx):
    if "966332497862484068" in str(ctx.message.author.roles):

        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid input, please follow the command with "load, unload or reload".')
    else:
        await ctx.send("You dont have the required role to access this command.")


@cog.command()
async def reload(ctx, cogname):
    if "966332497862484068" in str(ctx.message.author.roles):
        bot.unload_extension(f"cogs.{cogname}")
        bot.load_extension(f"cogs.{cogname}")
        await ctx.send(f"Successfully Reloaded {cogname}.")


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
