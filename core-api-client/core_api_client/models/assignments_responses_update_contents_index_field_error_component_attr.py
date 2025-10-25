from enum import Enum


class AssignmentsResponsesUpdateContentsINDEXFieldErrorComponentAttr(str, Enum):
    CONTENTS_INDEX_FIELD = "contents.INDEX.field"

    def __str__(self) -> str:
        return str(self.value)
