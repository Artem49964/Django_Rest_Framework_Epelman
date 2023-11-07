import os.path
from uuid import uuid1

from apps.core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar(instance: ProfileDataClass, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join(instance.surname, 'avatar', f'{uuid1()}.{ext}')
