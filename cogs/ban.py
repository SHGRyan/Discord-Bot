from discord.ext import commands
import discord

def cargos_permitidos(*nomes): 
    def check(ctx):
        return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @cargos_permitidos("💜Staff")
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        try:
            embed = discord.Embed(
                title="🚫 Você foi banido!",
                description=f"***Servidor:*** {ctx.guild.name} \n📝 ***Motivo***: {reason or 'Não especificado'}",
                color=discord.Color.red()
            )
            embed.set_footer(text="Caso tenha dúvidas, contate a moderação.")
            
            await member.send(embed=embed)
            await member.ban(reason=reason)
            canal_log = self.bot.get_channel(1359733487476670556)
            print("alguem usou comando pra banir.")
            await ctx.message.delete()
            if canal_log:
                await canal_log.send(f"📛 Usuário {member} foi banido do servidor {ctx.guild.name}! \n📝 Motivo: {reason or 'Não especificado'}")
        except Exception as e:
            await ctx.message.delete()
            await ctx.send(f"❌ Não foi possivel banir o usúario: {e}")

async def setup(bot):
    await bot.add_cog(Ban(bot))

