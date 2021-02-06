# bot.py
import os
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

playing_membmer = []
playing_membmer_profile = []


@client.event
async def on_ready():
    global playing_membmer
    print(f'{client.user} has connected')
    for guild in client.guilds:
        print(guild.name)
        for member in guild.members:
            if member.activity is not None and not member.bot:
                playing_membmer.append(member)
                playing_membmer_profile.append(await member.profile())

    print("hello")
    print(playing_membmer)
    print("hello")


client.run(TOKEN)


