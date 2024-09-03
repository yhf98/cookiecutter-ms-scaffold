from pydantic import BaseModel, ConfigDict, Field
from core.data_types import DatetimeStr
from .menu import MenuSimpleOut
from .dept import DeptSimpleOut

class Role(BaseModel):
    name: str
    disabled: bool = False
    order: int | None = None
    desc: str | None = None
    data_range: int = 4
    role_key: str
    is_admin: bool = False


class RoleSimpleOut(Role):
    model_config = ConfigDict(from_attributes=True)

    id: int
    create_at: DatetimeStr
    update_at: DatetimeStr


class RoleOut(RoleSimpleOut):
    model_config = ConfigDict(from_attributes=True)

    menus: list[MenuSimpleOut] = []
    depts: list[DeptSimpleOut] = []


class RoleIn(Role):
    menu_ids: list[int] = []
    dept_ids: list[int] = []


class RoleOptionsOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    label: str = Field(alias='name')
    value: int = Field(alias='id')
    disabled: bool

