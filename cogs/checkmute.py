import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class CheckMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="checkmute",
        description="Check muted members"
    )
    async def checkmute(self, ctx: SlashContext):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role:
            muted_members = [
                member for member in ctx.guild.members if mute_role in member.roles
            ]

            if muted_members:
                embed = discord.Embed(title="Muted Members", color=discord.Color.blurple())
                for member in muted_members:
                    embed.add_field(name="Member", value=member.display_name, inline=False)
                    embed.add_field(name="ID", value=member.id, inline=False)
                    embed.add_field(name="\u200b", value="\u200b", inline=False)  # Empty field for spacing

                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="No Muted Members",
                    description="There are no members currently muted.",
                    color=discord.Color.blurple()
                )
                await ctx.send(embed=embed)
        else:
            await ctx.send("Mute role does not exist.")

def setup(bot):
    bot.add_cog(CheckMute(bot))
