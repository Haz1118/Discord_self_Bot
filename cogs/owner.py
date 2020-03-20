import discord
from discord.ext import commands
import asyncio


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def 청소(self, ctx, num: int =1):
        await ctx.channel.purge(limit=num + 1)
        await ctx.send("청소완료!")
        await asyncio.sleep(1)
        await ctx.channel.purge(limit=1) 


def setup(bot):
    bot.add_cog(Owner(bot))