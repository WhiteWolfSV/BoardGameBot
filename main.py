from os import listdir
from discord.ext import commands
import discord
import config


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="_", intents=intents)
# Role id for bot master
botMasterRoleId = 966332497862484068

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
@commands.has_role(botMasterRoleId)
async def cog(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Invalid input, please follow the command with \"load, unload or reload\".")

@cog.command()
@commands.has_role(botMasterRoleId)
async def load(ctx, cogname):

    if str(botMasterRoleId) in str(ctx.message.author.roles):
        await bot.load_extension(f"cogs.{cogname}")
        await ctx.send(f"Successfully loaded {cogname}.")



@cog.command()
@commands.has_role(botMasterRoleId)
async def unload(ctx, cogname):

    if str(botMasterRoleId) in str(ctx.message.author.roles):
        await bot.unload_extension(f"cogs.{cogname}")
        await ctx.send(f"Successfully unloaded {cogname}.")



@cog.command()
@commands.has_role(botMasterRoleId)
async def reload(ctx, cogname):
    await bot.unload_extension(f"cogs.{cogname}")
    await bot.load_extension(f"cogs.{cogname}")
    await ctx.send(f"Successfully reloaded {cogname}.")


if __name__ == '__main__':
    bot.run(config.botToken)
