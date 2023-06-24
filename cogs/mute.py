import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from config import get_log_channel_id

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not mute_role:
            # Create the mute role if it doesn't exist
            mute_role = await ctx.guild.create_role(name="Muted", reason="Mute command")
            for channel in ctx.guild.channels:
                # Disable permission to send messages in all channels
                await channel.set_permissions(mute_role, send_messages=False)

        if mute_role not in member.roles:
            await member.add_roles(mute_role, reason=reason)
            log_channel_id = get_log_channel_id()
            if log_channel_id:
                log_channel = ctx.guild.get_channel(log_channel_id)
                if log_channel:
                    await log_channel.send(f'{member.mention} has been muted. Reason: {reason}')
            await ctx.send(f'{member.mention} has been muted. Reason: {reason}')
        else:
            await ctx.send(f'{member.mention} is already muted.')

    @cog_ext.cog_slash(
        name="mute",
        description="Mute a member",
        options=[
            create_option(
                name="member",
                description="The member to mute",
                option_type=6,
                required=True
            ),
            create_option(
                name="reason",
                description="Reason for muting",
                option_type=3,
                required=False
            )
        ]
    )
    async def mute_slash(self, ctx: SlashContext, member: discord.Member, reason=None):
        await self.mute(ctx, member, reason=reason)

def setup(bot):
    bot.add_cog(Mute(bot))
