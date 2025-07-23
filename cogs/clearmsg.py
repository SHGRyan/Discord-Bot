import discord
from discord.ext import commands

def cargos_permitidos(*nomes): 
    def check(ctx):
     return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)

class Clearmsg(commands.Cog): 
    def __init__(self, bot):
     self.bot = bot

    @commands.command() 
    @cargos_permitidos("💜Staff", "📞Atendentes", "🛠️ Técnico Discord") 
    async def clear(self, ctx):
       totalapagadas = 0
       try:
        while totalapagadas < 900:
         await ctx.send ("Limpando chat...")
         apagadas = await ctx.channel.purge(limit = 100)
         totalapagadas += apagadas
        print("alguem limpou o chat.") 
       except Exception as e:
          await ctx.message.delete()
          await ctx.send(f"❌ Erro ao limpar mensagens: {e}")


async def setup(bot): 
    await bot.add_cog(Clearmsg(bot))   