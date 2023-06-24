import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class ShowMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def showmute(self, ctx):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role:
            muted_members = [member for member in ctx.guild.members if mute_role in member.roles]
            if muted_members:
                embed = discord.Embed(title="Muted Members", color=discord.Color.blurple())
                for member in muted_members:
                    embed.add_field(name=member.display_name, value=member.id, inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No members are currently muted.")
        else:
            await ctx.send("Mute role does not exist.")

    @cog_ext.cog_slash(
        name="showmute",
        description="Show muted members",
    )
    async def showmute_slash(self, ctx: SlashContext):
        await self.showmute(ctx)

def setup(bot):
    bot.add_cog(ShowMute(bot))
