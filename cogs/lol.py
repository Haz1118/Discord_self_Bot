import discord
from discord.ext import commands
import bs4
from bs4 import BeautifulSoup
import urllib

class leagueoflegends(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 롤(self, ctx, nickname):
        location = nickname
        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)   

        bsObj = bs4.BeautifulSoup(html, "html.parser") 
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank3 = rank2.text
        print(rank3)

        if rank3 != 'Unranked':
            lolbed1 = discord.Embed(title='롤 정보',description='롤 정보입니다.',colour=discord.Colour.green())      
            lolbed1.add_field(name='당신의 티어', value=rank3, inline=False)
            lolbed1.add_field(name='-당신은 언랭-', value="표시할 전적이 없습니다.", inline=False)
            await ctx.send(embed=lolbed1)
        
        else:
            jumsu1 = rank1.find("div", {"class": "TierInfo"})
            jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
            jumsu3 = jumsu2.text
            jumsu4 = jumsu3.strip()#점수표시 (11LP등등)
            print(jumsu4)
 
            winlose1 = jumsu1.find("span", {"class": "WinLose"})
            winlose2 = winlose1.find("span", {"class": "wins"})
            winlose2_1 = winlose1.find("span", {"class": "losses"})
            winlose2_2 = winlose1.find("span", {"class": "winratio"})

            winlose2txt = winlose2.text
            winlose2_1txt = winlose2_1.text
            winlose2_2txt = winlose2_2.text #승,패,승률 나타냄  200W 150L Win Ratio 55% 등등
            print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

            lolbed2 = discord.Embed(title='롤 정보',description='롤 정보입니다.',colour=discord.Colour.green())
            lolbed2.add_field(name='당신의 티어', value=rank3, inline=False)
            lolbed2.add_field(name='당신의 LP(점수)', value=jumsu3, inline=False)
            lolbed2.add_field(name='당신의 승,패 정보', value=winlose2txt+" "+winlose2_1txt, inline=False)
            lolbed2.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
            await ctx.send(embed=lolbed2)

def setup(bot):
    bot.add_cog(leagueoflegends(bot))