from enum import Enum


class RegExEnum(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,19}$',
        'First letter uppercase min 2 max 25 ch',
    )

    PASSWORD = (
        r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$',
        [
            'min 1 lowercase ch',
            'min 1 uppercase ch',
            'min 1 digit',
            'min 1 special character',
            'length 8-30'
            ]
    )

    NAME = (
        r'^[A-Z][a-z]{2,49}$',
        'First letter must be upper case',
    )

    AGE = (
        r'^(0?[1-9]|[1-9][0-9]|[1][1-9][1-9]|200)$',
        'User must be older than 18',
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
