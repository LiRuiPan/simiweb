import json
from enum import (
    Enum,
    auto,
)


# 用户权限类
class UserRole(Enum):
    guest = auto()
    normal = auto()
    admin = auto()


class Encoder(json.JSONEncoder):
    prefix = "__enum__"

    def default(self, o):
        if isinstance(o, UserRole):
            return {self.prefix: o.name}
        else:
            return super().default(self, o)


def decode(d):
    if Encoder.prefix in d:
        name = d[Encoder.prefix]
        return UserRole[name]
    else:
        return d
