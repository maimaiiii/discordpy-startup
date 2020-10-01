from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 'ゴリラ'(ctx):
    await ctx.send('ゴリラじゃねぇ！ゴリラ人間です。')
    
@bot.command()
async def '休憩'(ctx):
    await ctx.send('お疲れ様！:cake:')

@bot.command()
async def 'ウホ'(ctx):
    await ctx.send('はぁはぁはぁ')
    
bot.run(token)
