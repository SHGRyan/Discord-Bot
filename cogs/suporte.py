import discord
from discord.ext import commands

ID_CANAL_TEXTO_TICKETS = (1359729246431609044)
ID_CANAL_VOZ_REUNIAO = (1360036009429176431)


class BotoesSuporte(discord.ui.View):
    @discord.ui.button(label="🎫 Tickets", style=discord.ButtonStyle.gray)
    async def ticket_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        canal = interaction.guild.get_channel(ID_CANAL_TEXTO_TICKETS)
        if canal:
            await interaction.response.send_message(
                f"Clique aqui para ir para o canal de tickets: {canal.mention}",
                ephemeral=True)
            

    @discord.ui.button(label="📞 Reunião/Call", style=discord.ButtonStyle.gray)
    async def reuniao_button(self, interaction: discord.Interaction, button: discord.ui.Button):
         canal = interaction.guild.get_channel(ID_CANAL_VOZ_REUNIAO)
         if canal:
            await interaction.response.send_message(
                f"Acesse o canal de voz para a reunião: {canal.mention}\n"
                "Clique no nome do canal e depois em **Ingressar** para entrar.",
                ephemeral=True)
            
class Suporte(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def suporte(self, ctx):
        print("Alguém precisa de suporte.")
        try:
            embed = discord.Embed(
                title="📞 **SUPORTE TÉCNICO**",
                description="Selecione o tipo de atendimento desejado abaixo:",
                color=discord.Color.light_gray()
            )
            view = BotoesSuporte()
            await ctx.send(embed=embed, view=view)
        except Exception as e:
            await ctx.send("Ocorreu um erro ao tentar enviar o painel de suporte.")

async def setup(bot):
    await bot.add_cog(Suporte(bot))
