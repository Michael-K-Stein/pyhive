from enum import Enum


class AssignmentsResponsesUpdateContentsINDEXContentErrorComponentAttr(str, Enum):
    CONTENTS_INDEX_CONTENT = "contents.INDEX.content"

    def __str__(self) -> str:
        return str(self.value)
