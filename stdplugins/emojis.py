"""Emoji
Available Commands:
.e s
.e apple
.e :/
. -_-"""
from telethon import events
import asyncio
from uniborg.util import admin_cmd


@borg.on(admin_cmd("e (.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "s":
        await event.edit("¯\_(ツ)_/¯")
    elif input_str == "apple":
        await event.edit("\uF8FF")
    elif input_str == ":/":
        await event.edit(input_str)
        animation_chars = [
            ":\\",
            ":/"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
    elif input_str == "-_-":
        await event.edit(input_str)
        animation_chars = [
            "-__-",
            "-_-"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 2])
