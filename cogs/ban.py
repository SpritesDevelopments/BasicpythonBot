import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from config import get_log_channel_id

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="ban", description="Ban a user")
    async def ban(self, ctx: SlashContext, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        log_channel_id = get_log_channel_id()
        if log_channel_id:
            log_channel = self.bot.get_channel(log_channel_id)
            if log_channel:
                await log_channel.send(f'{member} was banned. Reason: {reason}')
                await ctx.send(f'{member} was banned. Reason: {reason}')
            else:
                await ctx.send('Log channel not found.')
        else:
            await ctx.send('Log channel ID is not set.')

def setup(bot):
    bot.add_cog(Ban(bot))
