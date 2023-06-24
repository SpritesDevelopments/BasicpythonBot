import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class ShowMuteHistory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="showmutehistory",
        description="Show mute history for a user",
        options=[
            create_option(
                name="user",
                description="The user to show mute history",
                option_type=6,
                required=True
            )
        ]
    )
    async def showmutehistory(self, ctx: SlashContext, user: discord.Member):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role:
            embed = discord.Embed(
                title="Mute History",
                description=f"Mute history for {user.display_name}",
                color=discord.Color.blurple()
            )
            history = []
            for entry in user.guild.audit_logs(limit=10):
                if entry.action == discord.AuditLogAction.member_role_update and mute_role in entry.after.roles:
                    history.append(entry)
            
            if history:
                for entry in history:
                    moderator = entry.user
                    timestamp = entry.created_at.strftime("%Y-%m-%d %H:%M:%S")
                    embed.add_field(
                        name=f"{timestamp} - {moderator.display_name}",
                        value=f"Reason: {entry.reason}",
                        inline=False
                    )
            else:
                embed.add_field(
                    name="No History",
                    value="No mute history found for the user.",
                    inline=False
                )
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("Mute role does not exist.")

def setup(bot):
    bot.add_cog(ShowMuteHistory(bot))
