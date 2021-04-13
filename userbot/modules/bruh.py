import time
import subprocess
import asyncio
import sys
from os import environ, execle, remove
from userbot import (
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    UPSTREAM_REPO_BRANCH,
    UPSTREAM_REPO_URL,
)
from userbot.events import register


@register(outgoing=True, pattern=r"^\.kill$")
async def kills(killer):
    await killer.edit(f"Preparing to kill your ass... pls wait")
    time.sleep(3)
    await killer.edit(".")
    time.sleep(1)
    await killer.edit("..")
    time.sleep(1)
    await killer.edit("...")
    time.sleep(1)
    await killer.edit("Done preparing:D")
    time.sleep(2)
    await killer.edit("Killing you now")
    time.sleep(1)
    await killer.edit("BOOM!, your dead lmao")

