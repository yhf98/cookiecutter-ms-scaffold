from pydantic import BaseModel, ConfigDict
from core.data_types import DatetimeStr

class OperationRecord(BaseModel):
    phone: str | None = None
    user_id: int | None = None
    user_name: str | None = None
    status_code: int | None = None
    client_ip: str | None = None
    request_method: str | None = None
    api_path: str | None = None
    system: str | None = None
    browser: str | None = None
    summary: str | None = None
    route_name: str | None = None
    description: str | None = None
    tags: list[str] | None = None
    process_time: float | None = None
    params: str | None = None


class OperationRecordSimpleOut(OperationRecord):
    model_config = ConfigDict(from_attributes=True)

    create_at: DatetimeStr
