import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

class CreateMuteRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createmuterole(self, ctx):
        mute_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if mute_role:
            await ctx.send("Mute role already exists.")
        else:
            mute_role = await ctx.guild.create_role(name="Muted")
            await ctx.send(f"Mute role created with ID: {mute_role.id}")

        # Connect to the checkmute cog and update the mute role
        checkmute_cog = self.bot.get_cog("CheckMute")
        if checkmute_cog:
            checkmute_cog.set_mute_role(mute_role)

    @cog_ext.cog_slash(
        name="createmuterole",
        description="Create the mute role"
    )
    async def createmuterole_slash(self, ctx: SlashContext):
        await self.createmuterole(ctx)

def setup(bot):
    bot.add_cog(CreateMuteRole(bot))
