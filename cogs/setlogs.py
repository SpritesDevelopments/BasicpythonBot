import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option
from config import get_log_channel_id, set_log_channel_id

class SetLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setlogs(self, ctx, log_channel: discord.TextChannel):
        set_log_channel_id(log_channel.id)
        await ctx.send(f"Log channel set to {log_channel.mention}")

    @cog_ext.cog_slash(
        name="setlogs",
        description="Set the log channel for the bot",
        options=[
            create_option(
                name="log_channel",
                description="The channel to set as the log channel",
                option_type=7,
                required=True
            )
        ]
    )
    async def setlogs_slash(self, ctx: SlashContext, log_channel: discord.TextChannel):
        await self.setlogs(ctx, log_channel)

def setup(bot):
    bot.add_cog(SetLogs(bot))
