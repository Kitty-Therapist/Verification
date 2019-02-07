import discord
import asyncio
from discord.ext import commands

from Utils import Configuration

class Basic:
    def __init__(self,bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return
        if "Cereal is a soup" == message.content: #Bug Hunters
            user = message.author
            role = discord.utils.get(user.guild.roles, id=542626277052514314)
            await message.author.add_roles(role)
            await message.delete()
            reply = await message.channel.send(f"{user.mention}, you have recieved the {role.name} role!")
            await asyncio.sleep(10)
            await reply.delete()
        if "rowboat" == message.content: #Custodians
            user = message.author
            role = discord.utils.get(user.guild.roles, id=542626646943989760)
            await message.author.add_roles(role)
            await message.delete()
            reply = await message.channel.send(f"{user.mention}, you have recieved the {role.name} role!")
            await asyncio.sleep(10)
            await reply.delete()

    @commands.command()
    async def test(self, ctx: commands.Context):
        await ctx.send("I'm working!")

def setup(bot):
    bot.add_cog(Basic(bot))
