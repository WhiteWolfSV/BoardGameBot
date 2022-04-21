from discord.ext import commands


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stop(self, ctx):
        await ctx.send("Stopping all processes...")
        await self.bot.close()


def setup(bot):
    bot.add_cog(AdminCommands(bot))
