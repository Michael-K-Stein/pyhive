from enum import Enum


class HelpResponsesPartialUpdateContentsErrorComponentAttr(str, Enum):
    CONTENTS = "contents"

    def __str__(self) -> str:
        return str(self.value)
