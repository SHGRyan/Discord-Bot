import discord
from discord.ext import commands

def cargos_permitidos(*nomes): 
    def check(ctx):
     return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)

class Expulsar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @cargos_permitidos("💜Staff")
    async def expulsar(self, ctx, membro: discord.Member, *, motivo="Sem motivo informado"):
        try:
            await membro.kick(reason=motivo)
            await ctx.message.delete()
            canal_log = self.bot.get_channel(1359733487476670556)
            print("alguem usou comando para explulsar")
            if canal_log:     
             await ctx.send(f"👢 {membro.mention} foi expulso por. Motivo: {motivo}")
        except Exception as e:
            await ctx.message.delete()
            await ctx.send(f"❌ Erro ao expulsar: {e}")

async def setup(bot):
    await bot.add_cog(Expulsar(bot))
      
