from dataclasses import dataclass
from datetime import datetime


class ProfileDataClass:
    id: int
    name: str
    surname: str
    age: int


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: datetime
    created_ad: datetime
    updated_at: datetime
    profile: ProfileDataClass
