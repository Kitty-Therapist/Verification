import asyncio
import os
import sys
import time
import discord
import aiohttp
from datetime import datetime
from argparse import ArgumentParser
from discord.abc import PrivateChannel
from discord.ext import commands
import Utils
from Utils import Configuration

verificationbot = commands.Bot(command_prefix="!", case_insensitive=True)
verificationbot.STARTUP_COMPLETE = False

initial_extensions = ['Basic', 'Reload']

if __name__ == '__main__':
    for extension in initial_extensions:
        verificationbot.load_extension(f"cogs.{extension}")

@verificationbot.event
async def on_ready():
        print(f'\n\nLogged in as: {verificationbot.user.name} - {verificationbot.user.id}' + f'\nVersion: {discord.__version__}\n')
        await verificationbot.change_presence(activity=discord.Activity(name='the planning!!', type=discord.ActivityType.watching))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--token", help="Specify your Discord token")

    clargs = parser.parse_args()
    if 'verificationbotlogin' in os.environ:
        token = os.environ['verificationbotlogin']
    elif clargs.token:
        token = clargs.token
    elif not Configuration.get_master_var("LOGIN_TOKEN", "0") is "0":
        token = Configuration.get_master_var("LOGIN_TOKEN")
    else:
        token = input("Please enter your Discord token: ")
    verificationbot.run(token)
