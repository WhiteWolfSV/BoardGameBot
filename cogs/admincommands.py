from discord.ext.commands import has_permissions

from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(administrator=True)
    async def stop(self, ctx):
        await ctx.send("Stopping all processes...")
        await self.bot.close()


async def setup(bot):
    await bot.add_cog(AdminCommands(bot))
