import random

import discord
from discord.ui import Button, View
from discord.ext import commands
import asyncio
from os import listdir
from .classes import buttons
from discord.ext import commands


class HighLow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client = commands.bot

    @commands.command()
    async def hl(self, ctx):
        rndint = random.randint(0, 100)
        continueVar = True
        guessTries = 5
        print(rndint)

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower()

        await ctx.send(f"Please guess a number between 1 and 100. You have {guessTries} tries.")

        guessTries = guessTries - 1

        while continueVar:
            try:
                msg = await self.bot.wait_for("message", check=check, timeout=30)  # 30 seconds to reply
                if int(msg.content) < rndint:
                    await ctx.send("Your guess is lower.")
                elif int(msg.content) > rndint:
                    await ctx.send("Your guess is higher")
                else:
                    await ctx.send(f"Your guess {rndint} is correct!")
                    continueVar = False

                if guessTries != 0:
                    guessTries = guessTries - 1
                elif guessTries == 0 and continueVar != False:
                    await ctx.send(
                        f"You ran out of tries, the secret number was {rndint}.")
                    continueVar = False



            except asyncio.exceptions.TimeoutError:
                if continueVar:
                    await ctx.send("Sorry, you didn't reply in time.")
                else:
                    continueVar = False
            except ValueError:
                await ctx.send("Please send a valid number. (1-100)")
                guessTries = guessTries + 1


async def setup(bot):
    await bot.add_cog(HighLow(bot))
