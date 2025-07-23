import discord
from discord.ext import commands 

def cargos_permitidos(*nomes): 
    def check(ctx):
        return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)

class Repitirsay(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    @cargos_permitidos("💜Staff", "📞Atendentes", "🛠️ Técnico Discord")
    async def say(self, ctx, *, texto: str):
       try:
         print("O comando !say foi usado.")
         await ctx.message.delete()
         await ctx.send(texto)
       except Exception as e:
         await ctx.message.delete()
         print(f"❌ Erro ao repitir frase: {e}")

async def setup(bot): 
   await bot.add_cog(Repitirsay(bot))
          