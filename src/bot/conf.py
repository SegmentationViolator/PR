from operator import attrgetter
from typing import Any, Literal, Sequence
from cachetools import Cache, cachedmethod
from hikari import Snowflakeish, SnowflakeishSequence
from toml import load

from .util import report

FILENAME = "conf.toml"

_Conf = tuple[Snowflakeish, SnowflakeishSequence]
_ConfLookup = {
    "guild_id": 0,
    "role_ids": 1
}

def verify_conf(conf: dict[str, Any]) -> _Conf:
    guild_id: Snowflakeish = conf.get("guild_id") or report(KeyError("guild_id not found"))
    role_ids: SnowflakeishSequence = conf.get("role_ids") or report(KeyError("role_ids not found"))

    if not isinstance(guild_id, Snowflakeish):
        raise TypeError("guild_id is not snowflakish (integer)")

    elif not isinstance(role_ids, Sequence):
        raise TypeError("all role_ids are not snowflakish (integer)")
    
    elif len(role_ids) == 0:
        raise ValueError("role_ids is empty")

    elif not all(map(lambda role_id: isinstance(role_id, Snowflakeish), role_ids)):
        raise TypeError("all role_ids are not snowflakish (integer)")

    return guild_id, role_ids

class Conf:
    __slots__ = ["cache", "token"]
    cache: Cache

    def __init__(self, cache: Cache):
        self.cache = cache
        self.token = load(FILENAME).get("token") or report(KeyError("token not found"))

        if not isinstance(self.token, str):
            raise TypeError("token is not a string")

    @cachedmethod(attrgetter('cache'))
    def _view(self) -> _Conf:
        return verify_conf(load(FILENAME))

    def view(self, property: Literal["guild_id"] | Literal["role_ids"]) -> Snowflakeish | Sequence[Snowflakeish]:
        if _ConfLookup.get(property) is None:
            raise KeyError("invalid conf property")

        return self._view()[_ConfLookup[property]]
