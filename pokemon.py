from discord.ext import commands
import aiohttp, asyncio
from random import choice

class Pokemon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.website = "https://www.pokepedia.fr/Liste_des_Pokémon_dans_l'ordre_du_Pokédex_National"
    
    @commands.command()
    async def pokemon(self, ctx):
        """
        This procedure gonna get a image of pokemon ramdomly.
        """
        
        async with aiohttp.ClientSession() as session:
            async with session.get(self.website) as r:
                if r.status == 200:
                    res = []

                    html = await r.text()
                    code = html.split('\n')

                    for i in range(len(code)):
                        ligne = code[i].split('"')

                        for j in range(len(ligne)):
                            if len(ligne) > 2 and not(j + 2 >= len(ligne)) and ligne[j][1:] == ligne[j + 2]:
                                res.append(ligne[j])
                    
                    # The pokemon we choose ramdomly
                    which_pokemon = choice(res[12:])

                    print(which_pokemon)


            async with session.get('https://www.pokepedia.fr' + which_pokemon) as r:
                if r.status == 200:
                    res = []

                    html = await r.text()
                    code = html.split("\n")

                    for ligne in code:
                        for elmt in ligne.split('"'):
                            if '/image' in elmt and which_pokemon in elmt:
                                res.append(elmt)
                    
                    await ctx.send(res[0])

print(int(14/13))