from enum import Enum


class CourseProgramsUpdateAutoRoomErrorComponentAttr(str, Enum):
    AUTO_ROOM = "auto_room"

    def __str__(self) -> str:
        return str(self.value)
