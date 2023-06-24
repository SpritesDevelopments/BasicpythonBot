import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class BanHistory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def banhistory(self, ctx, user: discord.User):
        ban_entries = await ctx.guild.bans()
        user_bans = [ban_entry for ban_entry in ban_entries if ban_entry.user == user]
        if user_bans:
            embed = discord.Embed(title="Ban History", color=discord.Color.red())
            for ban_entry in user_bans:
                embed.add_field(name="User", value=f"{user.name}#{user.discriminator}", inline=False)
                embed.add_field(name="ID", value=user.id, inline=False)
                embed.add_field(name="Reason", value=ban_entry.reason, inline=False)
                embed.add_field(name="Moderator", value=ban_entry.user.name, inline=False)
                embed.add_field(name="\u200b", value="\u200b", inline=False)  # Empty field for spacing
            await ctx.send(embed=embed)
        else:
            await ctx.send("No ban history found for the specified user.")

    @cog_ext.cog_slash(
        name="banhistory",
        description="Show ban history for a user",
        options=[
            create_option(
                name="user",
                description="The user to show ban history for",
                option_type=6,
                required=True
            )
        ]
    )
    async def banhistory_slash(self, ctx: SlashContext, user: discord.User):
        await self.banhistory(ctx, user)

def setup(bot):
    bot.add_cog(BanHistory(bot))
