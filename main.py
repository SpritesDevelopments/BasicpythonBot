import discord
from discord.ext import commands
from discord_slash import SlashCommand
import asyncio
from config import TOKEN, get_log_channel_id

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.bans = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print('Loaded Sprites Basic Python Bot')
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
 

    # Load log channel ID on bot startup
    log_channel_id = get_log_channel_id()
    if log_channel_id is not None:
        log_channel = bot.get_channel(log_channel_id)
        if log_channel is not None:
            print(f'Log channel: {log_channel.name} ({log_channel.id})')
        else:
            print('Log channel not found')

initial_extensions = [
    'cogs.setlogs',
    'cogs.showban',
    'cogs.banhistory',
    'cogs.showmute',
    'cogs.checkmute',
    'cogs.ban',
    'cogs.unban',
    'cogs.mute',
    'cogs.unmute',
    'cogs.createmuterole',
    'cogs.botinfo',
    'cogs.help',
    'cogs.showmutehistory'
]

async def load_extensions():
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f'Loaded extension: {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(load_extensions())
    loop.run_until_complete(bot.start(TOKEN))
