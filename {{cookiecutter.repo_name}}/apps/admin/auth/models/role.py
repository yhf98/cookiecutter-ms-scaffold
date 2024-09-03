from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import String, Boolean, Integer
from .menu import AdminMenu
from .dept import AdminDept
from .m2m import admin_auth_role_menus, admin_auth_role_depts


class AdminRole(BaseModel):
    __tablename__ = "admin_auth_role"
    __table_args__ = ({'comment': '角色表'})

    name: Mapped[str] = mapped_column(String(50), index=True, comment="名称")
    role_key: Mapped[str] = mapped_column(String(50), index=True, comment="权限字符")
    data_range: Mapped[int] = mapped_column(Integer, default=4, comment="数据权限范围")
    disabled: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否禁用")
    order: Mapped[int | None] = mapped_column(Integer, comment="排序")
    desc: Mapped[str | None] = mapped_column(String(255), comment="描述")
    is_admin: Mapped[bool] = mapped_column(Boolean, comment="是否为超级角色", default=False)

    menus: Mapped[set[AdminMenu]] = relationship(secondary=admin_auth_role_menus)
    depts: Mapped[set[AdminDept]] = relationship(secondary=admin_auth_role_depts)
