import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(title="Bot Information", color=discord.Color.blurple())

        # Get bot stats
        total_guilds = len(self.bot.guilds)
        total_members = len(self.bot.users)
        total_commands = len(self.bot.commands)

        # Add fields to the embed
        embed.add_field(name="Total Guilds", value=total_guilds, inline=False)
        embed.add_field(name="Total Members", value=total_members, inline=False)
        embed.add_field(name="Total Commands", value=total_commands, inline=False)

        # Get server information
        server_list = "\n".join([guild.name for guild in self.bot.guilds])
        embed.add_field(name="Servers", value=server_list, inline=False)

        await ctx.send(embed=embed)

    @cog_ext.cog_slash(
        name="botinfo",
        description="Show bot information"
    )
    async def botinfo_slash(self, ctx: SlashContext):
        await self.botinfo(ctx)

def setup(bot):
    bot.add_cog(BotInfo(bot))
