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
        message = "Button Green"
        message1 = "Button Red"
        button1 = GrayButton(message)
        button2 = GrayButton(message1)

        async def button_callback1(interaction):
            button1 = GreenButton(message)
            view.clear_items()
            view.add_item(button1)
            await interaction.response.edit_message(view=view)

        async def button_callback2(interaction):
            view.children.remove()
            button2 = RedButton(message1)
            view.add_item(button2)
            await interaction.response.edit_message(view=view)

        button1.callback = button_callback1
        button2.callback = button_callback2

        view.add_item(button1)
        view.add_item(button2)
        await ctx.send("Test", view=view)


async def setup(bot):
    await bot.add_cog(HighLow(bot))