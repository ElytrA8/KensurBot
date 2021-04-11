from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.test (.*)")

async def test(event):
	await event.edit("this is a test command");
