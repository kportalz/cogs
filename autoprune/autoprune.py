import discord
from discord.ext import commands


class autoprune:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def prune(self):
        if ctx.message.author.server_permissions.administrator:
            msg = "You're an admin {0.author.mention}".format(ctx.message)
            await
            client.send_message(ctx.message.channel, msg)
        else:
            msg = "You're an average joe {0.author.mention}".format(ctx.message)
            await
            client.send_message(ctx.message.channel, msg)


def setup(bot):
    bot.add_cog(autoprune(bot))
