from enum import Enum


class ExercisePreviewTypes(str, Enum):
    DISABLED = "Disabled"
    MARKDOWN = "Markdown"
    PDF = "PDF"

    def __str__(self) -> str:
        return str(self.value)
