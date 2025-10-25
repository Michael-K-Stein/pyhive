from enum import Enum


class AssignmentsResponsesPartialUpdateContentsINDEXFieldErrorComponentAttr(str, Enum):
    CONTENTS_INDEX_FIELD = "contents.INDEX.field"

    def __str__(self) -> str:
        return str(self.value)
