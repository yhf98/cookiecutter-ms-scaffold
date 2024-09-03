from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr
from .issue import IssueSimpleOut

class IssueCategoryPlatformOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str | None = None
    platform: str | None = None
    is_active: bool | None = None
    create_user_id: int | None = None

    id: int
    update_at: DatetimeStr
    create_at: DatetimeStr

    issues: list[IssueSimpleOut] = None

