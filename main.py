from os import listdir
from discord.ext import commands
import discord
import config

<<<<<<< HEAD
intents = discord.Intents.all()

bot = commands.Bot(command_prefix="_", intents=intents)
# Role id for bot master
botMasterRoleId = 966332497862484068

=======
bot = commands.Bot(command_prefix="_")
masterRole = 966332497862484068
>>>>>>> 771a190f345d3508a380485722eb22b43db3634f

@bot.event
async def on_ready():
    print('Successfully logged in as {0.user}'.format(bot))
    # Loading all cogs in folder "cogs"
    for file in listdir('cogs'):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send(f"Missing arguments: `{error}`")
    else:
        await ctx.send(error)


# Commands to load, unload and reload extensions (cogs).
@bot.group()
@commands.has_role(masterRole)
async def cog(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid input, please follow the command with \"load, unload or reload\".")

@cog.command()
@commands.has_role(masterRole)
async def load(ctx, cogname):
<<<<<<< HEAD
    if str(botMasterRoleId) in str(ctx.message.author.roles):
        await bot.load_extension(f"cogs.{cogname}")
        await ctx.send(f"Successfully loaded {cogname}.")
=======
    bot.load_extension(f"cogs.{cogname}")
    await ctx.send(f"Successfully loaded {cogname}.")
>>>>>>> 771a190f345d3508a380485722eb22b43db3634f


@cog.command()
@commands.has_role(masterRole)
async def unload(ctx, cogname):
<<<<<<< HEAD
    if str(botMasterRoleId) in str(ctx.message.author.roles):
        await bot.unload_extension(f"cogs.{cogname}")
        await ctx.send(f"Successfully unloaded {cogname}.")
=======
    bot.unload_extension(f"cogs.{cogname}")
    await ctx.send(f"Successfully unloaded {cogname}.")
>>>>>>> 771a190f345d3508a380485722eb22b43db3634f


@cog.command()
async def reload(ctx, cogname):
    await bot.unload_extension(f"cogs.{cogname}")
    await bot.load_extension(f"cogs.{cogname}")
    await ctx.send(f"Successfully reloaded {cogname}.")


if __name__ == '__main__':
    bot.run(config.botToken)
