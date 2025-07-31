from discord.ext import commands
import discord
from datetime import datetime

class Hora(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hora(self, ctx):
     try:
       print("Alguem usou o comando !hora")
       data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       embed = discord.Embed(
       title="***Data e Hora Atual***",
       description="📆 Mostrando a data e hora atual:",
       color=discord.Color.dark_magenta()
    )
       
       embed.add_field(name="🕒 Data e Hora Atual", value=data_hora, inline=True)
     
     except Exception as e:
        await ctx.send(e)

       
     
     await ctx.send(embed=embed)
    
    

     

async def setup(bot):
   await bot.add_cog(Hora(bot))



