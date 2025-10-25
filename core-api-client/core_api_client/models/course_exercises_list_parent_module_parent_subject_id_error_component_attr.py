from enum import Enum


class CourseExercisesListParentModuleParentSubjectIdErrorComponentAttr(str, Enum):
    PARENT_MODULE_PARENT_SUBJECT_ID = "parent_module__parent_subject__id"

    def __str__(self) -> str:
        return str(self.value)
