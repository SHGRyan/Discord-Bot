from discord.ext import commands
import discord
import random

class Ppt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ppt(self, ctx, *, jogada: str):
        try:
            print("Usaram ppt.")
            jogada = jogada.lower()
            escolha = ["pedra", "papel", "tesoura"]
            jogada_bot = random.choice(escolha)

            if jogada not in escolha:
                embed = discord.Embed(
                    title="⚠️ Jogada inválida!",
                    description="Tente: **pedra**, **papel** ou **tesoura**.",
                    color=discord.Color.red()
                )
                embed.set_footer(text="📢 Dica: digite !ppt pedra | papel | tesoura")
                await ctx.send(embed=embed)
                return

            mensagem = ""
            cor = discord.Color.blue()

            if jogada_bot == "pedra" and jogada == "tesoura":
                mensagem = "✊🪨 Quebrei sua tesoura, eu venci essa rodada 😎 HAHAHA💥"
                cor = discord.Color.green()
            elif jogada_bot == "papel" and jogada == "pedra":
                mensagem = "✋🧻 Já vou usar esse papel higiênico pra me limpar hehe, SOU IMPARÁVEL HAHAHA 🔥"
                cor = discord.Color.green()
            elif jogada_bot == "tesoura" and jogada == "papel":
                mensagem = "✌️✂️ Tá fácil demais hein, tesourinha da SmartHelp é incrível demais 🤖"
                cor = discord.Color.green()
            elif jogada_bot == "tesoura" and jogada == "pedra":
                mensagem = "Ah, tentei com tesoura... 😭 Poxa, achei que ia ganhar. 💔"
                cor = discord.Color.red()
            elif jogada_bot == "pedra" and jogada == "papel":
                mensagem = "Peguei pedra... 😤 Já chega, não sou presente pra ficar embrulhando! 🤬"
                cor = discord.Color.red()
            elif jogada_bot == "papel" and jogada == "tesoura":
                mensagem = "Dessa vez escolhi papel... 🤬 Você venceu, mas quem manda aqui ainda sou EU! 😤"
                cor = discord.Color.red()
            elif jogada == jogada_bot:
                mensagem = "Empatamos! Fica olhando e me copiando é? 🙄"
                cor = discord.Color.gold()

            emojis = {
                "pedra": "✊",
                "papel": "✋",
                "tesoura": "✌️"
            }

            embed = discord.Embed(
                title="🎮 Pedra, Papel ou Tesoura!",
                description=mensagem,
                color=cor
            )

            embed.add_field(name="🧍‍♂️ Sua jogada", value=f"{emojis[jogada]} **{jogada.capitalize()}**", inline=True)
            embed.add_field(name="🤖 Jogada do Bot", value=f"{emojis[jogada_bot]} **{jogada_bot.capitalize()}**", inline=True)
            embed.set_footer(text=f"👤 Desafiado por: {ctx.author.display_name} | 🕹️ Jogue sempre que quiser!")

            await ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(f"❌ Erro ao iniciar ppt: {e}")
            return

async def setup(bot):
    await bot.add_cog(Ppt(bot))
