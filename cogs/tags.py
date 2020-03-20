import discord
from discord.ext import commands
import asyncio


class Tags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def on_reaction_add(reaction, user):
        if str(reaction.emoji) == ""