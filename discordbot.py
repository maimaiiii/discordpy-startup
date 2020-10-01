from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    await client.wait_until_ready()
    ch = client.get_channel()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def 'ゴリラ'(ctx):
    await ctx.send('ゴリラじゃねぇ！ゴリラ人間です。')
    
@bot.command()
async def '休憩'(ctx):
    await ctx.send('お疲れ様！')

@bot.command()
async def 'ウホ'(ctx):
    await ctx.send('はぁはぁはぁ')
    
@bot.command()
async def 'おはよう'(ctx):
    await ctx.send('ウホホホホ')
    
bot.run(token)
