from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="help",
        description="Show the available commands",
    )
    async def help(self, ctx: SlashContext):
        embed = discord.Embed(title="Basic Discord Bot - Help", description="Here are the available commands:", color=discord.Color.blurple())

        # Add commands and their descriptions
        embed.add_field(name="!setlogs", value="Set the log channel for the bot", inline=False)
        embed.add_field(name="!showban", value="Show the list of banned members", inline=False)
        embed.add_field(name="!banhistory", value="Show the ban history for a user", inline=False)
        embed.add_field(name="!showmute", value="Show the list of muted members", inline=False)
        embed.add_field(name="!checkmute", value="Check if members are currently muted", inline=False)
        embed.add_field(name="!ban", value="Ban a member from the server", inline=False)
        embed.add_field(name="!unban", value="Unban a member from the server", inline=False)
        embed.add_field(name="!mute", value="Mute a member in the server", inline=False)
        embed.add_field(name="!unmute", value="Unmute a member in the server", inline=False)
        embed.add_field(name="!createmuterole", value="Create a 'Muted' role for muting members", inline=False)
        embed.add_field(name="!botinfo", value="Get information about the bot and the server", inline=False)

        embed.set_footer(text="Powered by Sprites Developments Network | Visit our website at https://spritesdevelopmentsnetwork.co.uk/")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
