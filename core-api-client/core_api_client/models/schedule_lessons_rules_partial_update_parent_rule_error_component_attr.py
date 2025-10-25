from enum import Enum


class ScheduleLessonsRulesPartialUpdateParentRuleErrorComponentAttr(str, Enum):
    PARENT_RULE = "parent_rule"

    def __str__(self) -> str:
        return str(self.value)
