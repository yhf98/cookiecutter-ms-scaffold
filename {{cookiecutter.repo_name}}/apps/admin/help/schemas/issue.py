from typing import Optional
from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr
from apps.admin.auth.schemas import UserSimpleOut
from .issue_category import IssueCategorySimpleOut

class Issue(BaseModel):
    category_id: int | None = None
    create_user_id: int | None = None

    title: str | None = None
    content: str | None = None
    view_number: int | None = None
    is_active: bool | None = None


class IssueSimpleOut(Issue):
    model_config = ConfigDict(from_attributes=True)

    id: int
    update_at: DatetimeStr
    create_at: DatetimeStr


class IssueListOut(IssueSimpleOut):
    model_config = ConfigDict(from_attributes=True)

    create_user: UserSimpleOut
    category: IssueCategorySimpleOut
