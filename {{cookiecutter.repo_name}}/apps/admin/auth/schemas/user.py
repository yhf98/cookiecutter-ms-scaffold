from pydantic import BaseModel, ConfigDict, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from core.data_types import Telephone, DatetimeStr, Email
from .role import RoleSimpleOut
from .dept import DeptSimpleOut


class User(BaseModel):
    name: str
    phone: Telephone
    email: Email | None = None
    nickname: str | None = None
    avatar: str | None = None
    is_active: bool | None = True
    is_staff: bool | None = True
    gender: str | None = "0"
    is_wx_server_openid: bool | None = False


class UserIn(User):
    """
    创建用户
    """
    role_ids: list[int] = []
    dept_ids: list[int] = []
    password: str | None = ""


class UserUpdateBaseInfo(BaseModel):
    """
    更新用户基本信息
    """
    name: str
    phone: Telephone
    email: Email | None = None
    nickname: str | None = None
    gender: str | None = "0"


class UserUpdate(User):
    """
    更新用户详细信息
    """
    name: str | None = None
    phone: Telephone
    email: Email | None = None
    nickname: str | None = None
    avatar: str | None = None
    is_active: bool | None = True
    is_staff: bool | None = False
    gender: str | None = "0"
    role_ids: list[int] = []
    dept_ids: list[int] = []


class UserSimpleOut(User):
    model_config = ConfigDict(from_attributes=True)

    id: int
    update_at: DatetimeStr
    create_at: DatetimeStr

    is_reset_password: bool | None = None
    last_login: DatetimeStr | None = None
    last_ip: str | None = None


class UserPasswordOut(UserSimpleOut):
    model_config = ConfigDict(from_attributes=True)

    password: str


class UserOut(UserSimpleOut):
    model_config = ConfigDict(from_attributes=True)

    roles: list[RoleSimpleOut] = []
    depts: list[DeptSimpleOut] = []


class ResetPwd(BaseModel):
    password: str
    password_two: str

    @field_validator('password_two')
    def check_passwords_match(cls, v, info: FieldValidationInfo):
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('两次密码不一致!')
        return v
