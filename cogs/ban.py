import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from config import get_log_channel_id

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="ban",
        description="Ban a user",
        options=[
            create_option(
                name="user",
                description="The user to ban",
                option_type=6,
                required=True
            ),
            create_option(
                name="reason",
                description="Reason for the ban",
                option_type=3,
                required=False
            )
        ]
    )
    async def ban(self, ctx: SlashContext, user: discord.User, reason=None):
        member = ctx.guild.get_member(user.id)
        if member is not None:
            await member.ban(reason=reason)
            log_channel_id = get_log_channel_id()
            if log_channel_id:
                log_channel = self.bot.get_channel(log_channel_id)
                if log_channel:
                    await log_channel.send(f'{user} was banned. Reason: {reason}')
                    await ctx.send(f'{user} was banned. Reason: {reason}')
                else:
                    await ctx.send('Log channel not found.')
            else:
                await ctx.send('Log channel ID is not set.')
        else:
            await ctx.send('User not found in the server.')

def setup(bot):
    bot.add_cog(Ban(bot))
