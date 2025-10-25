from enum import Enum


class QueuesItemsUpdateSetModuleIdErrorComponentAttr(str, Enum):
    SET_MODULE_ID = "set_module_id"

    def __str__(self) -> str:
        return str(self.value)
