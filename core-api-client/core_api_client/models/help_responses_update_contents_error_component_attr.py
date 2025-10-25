from enum import Enum


class HelpResponsesUpdateContentsErrorComponentAttr(str, Enum):
    CONTENTS = "contents"

    def __str__(self) -> str:
        return str(self.value)
