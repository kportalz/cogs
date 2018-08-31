from discord.ext import commands
from __main__ import send_cmd_help
from cogs.utils import checks


# by kevin portalz for tt
class strikeout:
    def __init__(self, bot):
        self.bot = bot

    @checks.admin_or_permissions(ADMINISTRATOR=True)
    @commands.group(name="strike", pass_context=True)
    async def _strike(self, ctx):
        """Prune members"""
        if ctx.invoked_subcommand is None:
            await
            send_cmd_help(ctx)


def check_folder():
    if not os.path.exists("data/strikeout"):
        print("Creating data/strikeout folder...")
        os.makedirs("data/strikeout")


def check_file():
    strikes = []

    f = "data/strikeout/strikes.json"
    if not fileIO(f, "check"):
        print("Creating default strikes.json...")
        fileIO(f, "save", strikes)


def setup(bot):
    check_folder()
    check_file()
    n = strikeout(bot)
    bot.add_cog(n)
