#####################################################################################


import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.members = True  # Permite acesso aos eventos de membros, como "on_member_join"
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Serviços ativados! O pai tá on Ryan Nogueira!")
    print("📋 Comandos registrados:")
    for command in bot.commands:
        print(f" - {command.name}")

async def load_cogs():  
    for filename in os.listdir('./cogs'): 
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}') 
                print(f'✅ Cog carregado: {filename}')
            except Exception as e:
                print(f'❌ Erro ao carregar {filename}: {e}')

if __name__ == "__main__":
    async def main():
        await load_cogs()
        await bot.start(token)
    asyncio.run(main())