import discord
from discord.ext import commands
import asyncio
import random



class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 안녕(self, ctx):
        rand = random.randrange(1,4)
        if rand == 1:
            await ctx.send('안녕!, 세상')
        elif rand == 2:
            await ctx.send('뭐')
        elif rand == 3:
            await ctx.send('당근당근')

    @commands.command()
    async def 초대(self, ctx):
        serbed = discord.Embed(title="디스코드", color=0x0000)
        serbed.add_field(name="초대링크",value="https://discord.gg/8eRT2FZ", inline=False)
        serbed.set_footer(text="이 링크는 만료되지 않습니다.")
        await ctx.send(embed=serbed)

    @commands.command()
    async def 핑(self, ctx):
        latancy = self.bot.latency
        await ctx.send(f':ping_pong: ! : {round(latancy * 1000)}ms')

    @commands.command()
    async def 투표(self, ctx, votecount = 'bool'):
        if votecount.lower() == 'bool':
            emote_list = ['✅', '❌']
        elif votecount in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            emotes = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']
            emote_list = []
            for i in range (0, int(votecount)):
                emote_list.append(emotes[i])
        else:
            await ctx.send(':x: 숫자를 2 ~ 10 까지중에 정해주세요')

        message = await ctx.channel.history(limit=1, before=ctx.message).flatten()
        try:
            await ctx.message.delete()
        except:
            pass

        for emote in emote_list:
            await message[0].add_reaction(emote)

def setup(bot):
    bot.add_cog(Command(bot))