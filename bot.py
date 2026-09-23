import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise SystemExit("DISCORD_TOKEN is not set. Copy .env.example to .env and paste your bot token.")

intents = discord.Intents.default()
intents.message_content = True  # also enable this in the Developer Portal

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is online and ready.")


@bot.command(name="ping")
async def ping(ctx: commands.Context):
    """Check the bot is alive: !ping -> Pong!"""
    await ctx.send("Pong!")


@bot.command(name="hello")
async def hello(ctx: commands.Context):
    """Say hi back: !hello -> Hello, <name>!"""
    await ctx.send(f"Hello, {ctx.author.display_name}!")


if __name__ == "__main__":
    bot.run(TOKEN)
