import random, os, aiohttp
from youtube import Youtube
from music import Music
from pokemon import Pokemon
from discord.ext import commands
import discord

token = "ODA4MDc1NzM0MjA3ODIzODgy.YCBRLA._QIyabQXUqo_7fXG0immeFpjIL4"

bot = commands.Bot(command_prefix="$")
 
# Mettre les commandes
bot.add_cog(Music(bot))
bot.add_cog(Youtube(bot))
bot.add_cog(Pokemon(bot))

@bot.event
async def on_ready():
    print("Bon pret")
    
    # default command
    activite = "Maitre du monde"
    
    # get an activity
    if os.path.exists('file/activity.txt'):
        with open('file/activity.txt', 'r+') as f:
            activite = random.choice(f.readlines())
            f.close()

    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(activite))

@bot.command()
async def test(ctx, *, arg):
    """
    When you want the bot to say something
    """
    # Just for me
    droit = ['Tsurea#4343']


    if str(ctx.author) in droit:                                                                                                                     
        await ctx.send(arg)
    else:
        await ctx.send(f"{ctx.author} wesh t'es qui")

@bot.command()
async def hello(ctx):
    """
    If someone want to say hi
    """
    res = "Salut"

    if os.path.exists("file/hello.txt"):
        with open('file/hello.txt', "r+") as idea:
            res = random.choice(idea.readlines())
            print(res)
            idea.close()
    
    await ctx.send(res)        

@bot.command()
async def cat(ctx):
    """
    Go get a picture of a cat
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js['file'])

if "__main__" == __name__:
    bot.run(token)
