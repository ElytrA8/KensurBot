# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the server. """

from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from os import remove
from platform import python_version, uname
from shutil import which
import json
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz
from requests import get

from telethon import version

from userbot import ALIVE_NAME, CMD_HELP, KENSURBOT_VERSION, WEATHER_DEFCITY
from userbot import OPEN_WEATHER_MAP_APPID as OWM_API
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = ALIVE_NAME or "Set `ALIVE_NAME` ConfigVar!"
# ============================================

# ===== CONSTANT =====
DEFCITY = WEATHER_DEFCITY or None

@register(outgoing=True, pattern=r"^\.bot(?: |$)(.*)")
async def amireallyalive(alive):

    APPID = OWM_API

    if not OWM_API:
        return await alive.edit(
            "**Get an API key from** https://openweathermap.org **first.**"
        )

    APPID = OWM_API

    anonymous = False

    if not alive.pattern_match.group(1):
        CITY = DEFCITY
    elif alive.pattern_match.group(1).lower() == "anon":
        CITY = DEFCITY
        anonymous = True
    else:
        CITY = alive.pattern_match.group(1)

    if not CITY:
        return await alive.edit(
            "**Please specify a city or set one as default using the WEATHER_DEFCITY config variable.**"
        )

    timezone_countries = {
        timezone: country
        for country, timezones in c_tz.items()
        for timezone in timezones
    }


    if "," in CITY:
        newcity = CITY.split(",")
        if len(newcity[1]) == 2:
            CITY = newcity[0].strip() + "," + newcity[1].strip()
        else:
            country = await get_tz((newcity[1].strip()).title())
            try:
                countrycode = timezone_countries[f"{country}"]
            except KeyError:
                return await alive.edit("**Invalid country.**")
            CITY = newcity[0].strip() + "," + countrycode.strip()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}"
    request = get(url)
    result = json.loads(request.text)

    if request.status_code != 200:
        return await alive.edit("**Invalid country.**")

    curtemp = result["main"]["temp"]

    def fahrenheit(f):
        temp = str((f - 273.15) * 9 / 5 + 32).split(".")
        return temp[0]

    def celsius(c):
        temp = str(c - 273.15).split(".")
        return temp[0]


    """ For .alive command, check if the bot is running.  """
    await alive.edit(
        f"**KensurBot v{KENSURBOT_VERSION} is up and running!**\n\n"
        f"This is a unoffical version of the KensurBot made by\n"
        f"the great just6chill\n\n"
        f"**Telethon:** {version.__version__}\n"
        f"**Python:** {python_version()}\n"
        f"**User:** {DEFAULTUSER}\n"
        f"**City:** {WEATHER_DEFCITY}\n\n"
        f"**current weather in {WEATHER_DEFCITY}:** {celsius(curtemp)}°C | {fahrenheit(curtemp)}°F\n"
    )