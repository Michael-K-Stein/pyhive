from enum import Enum


class CourseProgramsPartialUpdateHanichClassesOnlyErrorComponentAttr(str, Enum):
    HANICH_CLASSES_ONLY = "hanich_classes_only"

    def __str__(self) -> str:
        return str(self.value)
