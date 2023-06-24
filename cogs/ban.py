import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from config import LOG_CHANNEL_ID

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ban", description="Ban a user")
    async def ban(self, ctx: SlashContext, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            await log_channel.send(f'{member} was banned. Reason: {reason}')
            await ctx.send(f'{member} was banned. Reason: {reason}')
        else:
            await ctx.send('Log channel not found.')

def setup(bot):
    bot.add_cog(Ban(bot))
