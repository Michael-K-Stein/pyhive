from enum import Enum


class QueuesItemsPartialUpdateSetModuleIdErrorComponentAttr(str, Enum):
    SET_MODULE_ID = "set_module_id"

    def __str__(self) -> str:
        return str(self.value)
