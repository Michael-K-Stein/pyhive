from enum import Enum


class AssignmentsResponsesCreateContentsINDEXFieldErrorComponentAttr(str, Enum):
    CONTENTS_INDEX_FIELD = "contents.INDEX.field"

    def __str__(self) -> str:
        return str(self.value)
