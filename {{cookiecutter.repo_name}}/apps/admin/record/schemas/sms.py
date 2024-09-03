from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr

class SMSSendRecord(BaseModel):
    phone: str
    status: bool = True
    user_id: int | None = None
    content: str | None = None
    desc: str | None = None
    scene: str | None = None


class SMSSendRecordSimpleOut(SMSSendRecord):
    id: int
    create_at: DatetimeStr
    update_at: DatetimeStr

    model_config = ConfigDict(from_attributes=True)
