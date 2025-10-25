from enum import Enum


class CourseProgramsPartialUpdateAutoRoomErrorComponentAttr(str, Enum):
    AUTO_ROOM = "auto_room"

    def __str__(self) -> str:
        return str(self.value)
