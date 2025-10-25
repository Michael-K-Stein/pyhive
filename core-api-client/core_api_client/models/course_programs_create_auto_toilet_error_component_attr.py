from enum import Enum


class CourseProgramsCreateAutoToiletErrorComponentAttr(str, Enum):
    AUTO_TOILET = "auto_toilet"

    def __str__(self) -> str:
        return str(self.value)
