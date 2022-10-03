from asyncio import sleep
from random import randint
from cachetools import TTLCache
from crescent import Bot, event
from hikari import Color, Snowflake, StartedEvent

from .conf import Conf
from .util import calculate_interval, report

conf = Conf(TTLCache(1, 900))
bot = Bot(conf.token)

@bot.include
@event(event_type=StartedEvent)
async def on_ready(event: StartedEvent):
    # Verify that bot is only in one guild that is specified in conf.toml
    guild = conf.view("guild_id")
    guild_object = await bot.rest.fetch_guild(guild)

    guild_role_objects = guild_object.get_roles()
    prismatic_roles: list[Snowflake] = []

    for role_id in conf.view("role_ids"):
        prismatic_roles.append(guild_role_objects.get(role_id).id or report(ValueError("invalid role_id was passed")))

    del guild_object
    del guild_role_objects

    interval = calculate_interval(len(prismatic_roles))

    while bot.is_alive:
        for role in prismatic_roles:
            await bot.rest.edit_role(guild, role, color=Color(randint(0x0, 0xFFFFFF)))
        await sleep(interval)

bot.run()
