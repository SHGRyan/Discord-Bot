import discord
from discord.ext import commands

class Bemvindomsg(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener() 
    async def on_member_join(self, member):
    
     bemvindomsg = discord.utils.get(member.guild.text_channels, name="💬・𝖻𝖾𝗆-𝗏𝗂𝗇𝖽𝗈")  
    
     if bemvindomsg:

        embed = discord.Embed(

            title=(f"👋 ***Bem-vindo ao servidor oficial da SmartHelp!*** {member}"),
            description=(f"📌 Este é o seu ponto de apoio técnico confiável. Atuamos com suporte remoto especializado para empresas de pequeno e médio porte, oferecendo soluções rápidas e eficientes em diversas áreas da tecnologia.\n💡 O que você encontrará aqui:\n• Atendimento 24h com técnicos qualificados\n• Suporte com instalação e manutenção de sistemas\n• Diagnósticos e análises completas de hardware e software\n• Suporte em linguagens de programação e sistemas web\n• Atendimentos via Discord, AnyDesk, WhatsApp e site\n🔒 Importante: Antes de utilizar nossos serviços, acesse os canais <>, <#1359718322194878606>, <#1354533606994870347> e <#1360069286122750023> para se informar e configurar seu acesso corretamente.\n✅ Primeiro atendimento é gratuito. Aproveite para conhecer nosso modelo de suporte!\nSeja muito bem-vindo(a)! Estamos prontos para ajudar. 🚀"),
           
            color=discord.Color.blue()
        )

        embed.set_image(url="https://i.pinimg.com/originals/21/11/61/21116158daaeb1459b4ec0758505e1ad.gif") 
        
        await bemvindomsg.send(embed=embed)


async def setup(bot):
   await bot.add_cog(Bemvindomsg(bot))
      