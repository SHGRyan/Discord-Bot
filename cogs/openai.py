import discord
from discord.ext import commands
import openai
import os

def cargos_permitidos(*nomes): 
    def check(ctx):
     return any(role.name in nomes for role in ctx.author.roles)
    return commands.check(check)

class Gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        openai.api_key = os.getenv("OPENAI_KEY")

    @commands.command()
    @cargos_permitidos("💜Staff", "📞Atendentes", "✍️Assinantes", "🛠️ Técnico Discord", "🧑‍💻Técnico Developer", "🔧Técnico OS", "🖥️Técnico de Hardware")
    async def ia(self, ctx, *, pergunta: str):
        print("alguem usou a ia.")
        await ctx.send("💭 Pensando...")
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente útil no Discord."}, #aqui você coloca o foco que vc desejar para sua IA. Você contextualiza ele.
                    {"role": "user", "content": pergunta}
                ]
            )
            resposta = response['choices'][0]['message']['content']
            await ctx.send(resposta)
        except Exception as e:
            await ctx.send("⚠️ Erro ao gerar resposta.")
            print(f"Erro IA: {e}")

async def setup(bot):
    await bot.add_cog(Gpt(bot))