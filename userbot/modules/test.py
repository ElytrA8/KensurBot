from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.setbio (.*)")

async def test(event):
	await event.edit("this is a test command");