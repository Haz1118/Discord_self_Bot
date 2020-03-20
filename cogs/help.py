import discord
from discord.ext import commands
import asyncio

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 도움말(self, ctx):
        helpbed = discord.Embed(title='도움말',description='롤 정보입니다.',colour=discord.Colour.green())
        helpbed.add_field(name = "!안녕",value = "인사를 해줍니다.",inline=False)
        helpbed.add_field(name = "!초대",value = "초대링크를 알려드려요!.",inline=False)
        helpbed.add_field(name = "!청소",value = "(!청소 숫자) 를 이용해 채팅을 지우세요!",inline=False)
        helpbed.add_field(name = "!핑",value = "핑을 체크 합니다.",inline=False)
        helpbed.add_field(name = "!날씨 ",value = "(!날씨 지역)을 사용하시면 날씨를 알 수 있습니다.",inline=False)
        helpbed.add_field(name = "!롤",value = "(!롤 닉네임)을 사용하여 당신의 전적을 확인하세요!",inline=False) 
        helpbed.add_field(name = "!코로나현황",value = "현재 코로나 현황을 확인합니다.",inline=False)   
        await ctx.send(embed = helpbed)

def setup(bot):
    bot.add_cog(Help(bot))