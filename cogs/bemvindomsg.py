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
            description=(f"Seja bem vindo ao nosso servidor!✅"),
           
            color=discord.Color.blue()
        )

        embed.set_image(url="https://i.pinimg.com/originals/21/11/61/21116158daaeb1459b4ec0758505e1ad.gif") 
        
        await bemvindomsg.send(embed=embed)


async def setup(bot):
   await bot.add_cog(Bemvindomsg(bot))
      