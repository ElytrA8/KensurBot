#me command by just6chill

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.me$")

async def me(event):
	await event.edit("https://github.com/just6chill");