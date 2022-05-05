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