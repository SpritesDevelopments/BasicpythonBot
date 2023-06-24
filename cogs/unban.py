import discord
from discord.ext import commands
from config import LOG_CHANNEL_ID

class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unban(self, ctx, member_id: int, reason=None):
        banned_users = await ctx.guild.bans()
        member = discord.utils.find(lambda u: u.user.id == member_id, banned_users)
        await ctx.guild.unban(member.user, reason=reason)
        log_channel = self.bot.get_channel(LOG_CHANNEL_ID)
        await log_channel.send(f'{member.user} was unbanned. Reason: {reason}')

def setup(bot):
    bot.add_cog(Unban(bot))
