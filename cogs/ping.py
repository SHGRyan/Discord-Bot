from discord.ext import commands

class Ping(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
      print("Alguem usou o ping pong!")
      await ctx.send(":ping_pong: Pong!")

async def setup(bot): 
    await bot.add_cog(Ping(bot))

