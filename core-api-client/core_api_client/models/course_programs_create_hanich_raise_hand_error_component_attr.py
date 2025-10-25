from enum import Enum


class CourseProgramsCreateHanichRaiseHandErrorComponentAttr(str, Enum):
    HANICH_RAISE_HAND = "hanich_raise_hand"

    def __str__(self) -> str:
        return str(self.value)
