from enum import Enum


class ErrorCode415Enum(str, Enum):
    UNSUPPORTED_MEDIA_TYPE = "unsupported_media_type"

    def __str__(self) -> str:
        return str(self.value)
