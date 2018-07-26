import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks


class autoprune:

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def estprune(self, days=30):
        """Estimate count of members that would be pruned based on the amount of days. Staff only."""
        if days > 30:
            await
            self.bot.say("Maximum 30 days")
            return
        if days < 1:
            await
            self.bot.say("Minimum 1 day")
            return
        msg = await
        self.bot.say("I'm figuring this out!".format(self.bot.server.name))
        count = await
        self.bot.estimate_pruned_members(server=self.bot.server, days=days)
        await
        self.bot.edit_message(msg, "{:,} members inactive for {} day(s) would be kicked from {}!".format(count, days, self.bot.server.name))


def setup(bot):
    bot.add_cog(autoprune(bot))
