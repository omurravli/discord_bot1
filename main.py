import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

bot.run("discord_token")

#hello world