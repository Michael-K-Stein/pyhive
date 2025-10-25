from enum import Enum


class CourseProgramsListIdInErrorComponentAttr(str, Enum):
    ID_IN = "id__in"

    def __str__(self) -> str:
        return str(self.value)
