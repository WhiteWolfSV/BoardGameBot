import discord
from discord.ui import Button, View
from discord.ext import commands


class BlueButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)


class GreenButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green)


class RedButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.red)


class GrayButton(Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.gray)


class HighLow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hl(self, ctx, message="Default"):
        view = View()
        button = GrayButton(message)

        async def button_callback(interaction):
            button = GreenButton(message)
            view.clear_items()
            view.add_item(button)
            await interaction.response.edit_message(view=view)

        button.callback = button_callback

        view.add_item(button)
        await ctx.send("Test", view=view)


async def setup(bot):
    await bot.add_cog(HighLow(bot))
