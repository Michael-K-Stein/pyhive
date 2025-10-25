from enum import Enum


class CourseProgramsCreateAutoToiletCountErrorComponentAttr(str, Enum):
    AUTO_TOILET_COUNT = "auto_toilet_count"

    def __str__(self) -> str:
        return str(self.value)
