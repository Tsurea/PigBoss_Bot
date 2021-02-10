import discord
from discord.ext import commands

class Command(commands.Bot(command_prefix='$')):
    def __init__(self):
        token = "ODA4MDc1NzM0MjA3ODIzODgy.YCBRLA._QIyabQXUqo_7fXG0immeFpjIL4"

        print('Lancement du bot')

    async def on_ready(self):
        print("Bon pret")
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game("Lisez Blue lock"))

    async def regles(self, ctx, new: discord.Member):
        await ctx.send("Bah amuser vous les gens (interdit de spam pour SolDavid)")

    async def bienvenue(self, ctx, new: discord.Member):
        pseudo = new.mention
        await ctx.send(f"Bienvenue à {pseudo} sur le serveur discord! N'oublie pas de faire $regles")

bg = Command()
bg.run("ODA4MDc1NzM0MjA3ODIzODgy.YCBRLA._QIyabQXUqo_7fXG0immeFpjIL4")