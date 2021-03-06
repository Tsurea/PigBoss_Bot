from urllib.request import urlopen
from discord.ext import commands
import requests

# Url pour les liens
search = "https://www.youtube.com/results?search_query="
site = "https://www.youtube.com/"

# recherche des liens grace à href
user_ = 'user/'
watch_ = '/watch?v='


class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def traduire(self, message):
        """
        Cette fonction sert à traduire le message pour en faire une recherche sur youtube.

        param message: list de str
        return: str
        """

        # Si il y a juste un element
        if not len(message) == 1:
            return "+".join(message)
        else:
            return message[0]

    def extraire(self, url, prefix):
        """
        Cette fonction extrait les liens de la page web

        param url: str, le lien d'une recherche sur youtube
        param prefix: str
        return: str, le lien
        """
        # Recuperer le code html de la page youtube
        print(url)
        code = urlopen(url).read().decode('utf8').split('"')

        for elmt in code:
            if prefix in elmt:
                return elmt
        
        # Valeur par defaut
        return '/watch?v=jNQXAC9IVRw'

    @commands.command()
    async def video(self, ctx, *, arg: str):
        """
        Envoie un lien de video youtube
        """
        await ctx.send(site + self.extraire(search + self.traduire(arg.split(' ')), watch_))

    @commands.command()
    async def chaine(self, ctx, *, arg):
        """
        Envoie le chaine youtube demandé
        """
        await ctx.send(site + self.extraire(search + self.traduire(arg.split(' ')), user_))