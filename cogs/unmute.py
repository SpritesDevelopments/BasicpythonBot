import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from config import get_log_channel_id

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role and mute_role in member.roles:
            await member.remove_roles(mute_role)
            log_channel_id = get_log_channel_id()
            if log_channel_id:
                log_channel = ctx.guild.get_channel(log_channel_id)
                if log_channel:
                    await log_channel.send(f'{member.mention} has been unmuted.')
            await ctx.send(f'{member.mention} has been unmuted.')
        else:
            await ctx.send(f'{member.mention} is not muted.')

    @cog_ext.cog_slash(
        name="unmute",
        description="Unmute a member",
        options=[
            create_option(
                name="member",
                description="The member to unmute",
                option_type=6,
                required=True
            )
        ]
    )
    async def unmute_slash(self, ctx: SlashContext, member: discord.Member):
        await self.unmute(ctx, member)

def setup(bot):
    bot.add_cog(Unmute(bot))
