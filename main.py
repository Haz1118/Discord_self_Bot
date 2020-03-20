import discord
from discord.ext import commands
from discord.ext.commands import bot
import os
import sys, traceback

token = 'Njg4MDA3MDU2MzkyOTc4NDQz.XnNi8w.Fp719IprF-jNeeaN2WV-1_3vaAQ'

bot = commands.Bot(command_prefix="!")

bot.remove_command('help')

initial_extensions = ['cogs.corona',
                      'cogs.help',
                      'cogs.commands',
                      'cogs.lol',
                      'cogs.weather',
                      'cogs.owner']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print("디스코드 봇 실행완료")
    print(bot.user.name)
    print(bot.user.id)
    print('---------')
    await bot.change_presence(activity=discord.Game(name='Cogs testing'))
    
bot.run(token)
