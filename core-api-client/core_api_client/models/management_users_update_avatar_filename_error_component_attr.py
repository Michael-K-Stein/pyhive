from enum import Enum


class ManagementUsersUpdateAvatarFilenameErrorComponentAttr(str, Enum):
    AVATAR_FILENAME = "avatar_filename"

    def __str__(self) -> str:
        return str(self.value)
