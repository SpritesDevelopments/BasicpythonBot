import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class ShowBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def showban(self, ctx):
        bans = await ctx.guild.bans()
        if bans:
            embed = discord.Embed(title="Banned Users", color=discord.Color.red())
            for ban_entry in bans:
                user = ban_entry.user
                embed.add_field(name="User", value=f"{user.name}#{user.discriminator}", inline=False)
                embed.add_field(name="ID", value=user.id, inline=False)
                embed.add_field(name="Reason", value=ban_entry.reason, inline=False)
                embed.add_field(name="\u200b", value="\u200b", inline=False)  # Empty field for spacing
            await ctx.send(embed=embed)
        else:
            await ctx.send("No users are currently banned.")

    @cog_ext.cog_slash(
        name="showban",
        description="Show banned users",
    )
    async def showban_slash(self, ctx: SlashContext):
        await self.showban(ctx)

def setup(bot):
    bot.add_cog(ShowBan(bot))
