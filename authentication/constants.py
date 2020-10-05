from enum import Enum

CHAR_LEN_MAX = 500
CHAR_LEN_MIN = 150
CHAR_LEM_NORM = 250
STRING_LEN_MAX = 5000
SESSION_EXPIRATION_TIME = (0, 15, 0, 0)
OT_TOKEN_EXPIRATION_TIME = (0, 0, 15, 0)
AUTH_TOKEN_EXPIRATION_TIME = (0, 0, 15, 0)


class UserAccountActionEnum(Enum):
    UNSUCCESSFUL_LOGIN = 1
    FIRST_LOGIN = 2
    LOGIN = 3
    RESET_PASSWORD = 4
    REGISTER = 5
    UNSUCCESSFUL_REGISTER = 6
    LOGOUT = 7
    UNSUCCESSFULL_RESET_PASSWORD = 8

    @classmethod
    def members(cls):
        return [(e.value, e.name) for e in cls]

    @classmethod
    def format(cls, value):
        return cls(value).name


class UserActionRoleEnum(Enum):
    VISITOR = 1
    EXHIBITOR = 2
    ORGANIZER = 3
    SPEAKER = 4

    @classmethod
    def members(cls):
        return [(e.value, e.name) for e in cls]

    @classmethod
    def format(cls, value):
        return cls(value).name

