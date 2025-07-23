from discord.ext import commands
import discord

def cargos_permitidos(*nomes): 
    def check(ctx):
     return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)


class Comissao(commands.Cog):
    def __init__(self, bot):
     self.bot = bot
    @commands.command()
    @cargos_permitidos("💜Staff")
    async def comissao(self ,ctx , valor: float):
       try:
          valor_comissao = valor * 20 / 100 #(20 é a porcentagem de comissao.)
          await ctx.send(f"A comissão recebida por esse funcionário de acordo com o valor do projeto será: R${valor_comissao:.2f}💵")
       except Exception as e:
          await ctx.send(e)


async def setup(bot):
    await bot.add_cog(Comissao(bot))
      
#calcula a comissao d funcionarios do meu server btg supremo

         
    
      


