from db.db_base import Base
from sqlalchemy import ForeignKey, Column, Table, Integer


admin_auth_user_roles = Table(
    "admin_auth_user_roles",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("admin_auth_user.id", ondelete="CASCADE")),
    Column("role_id", Integer, ForeignKey("admin_auth_role.id", ondelete="CASCADE")),
)


admin_auth_role_menus = Table(
    "admin_auth_role_menus",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("admin_auth_role.id", ondelete="CASCADE")),
    Column("menu_id", Integer, ForeignKey("admin_auth_menu.id", ondelete="CASCADE")),
)

admin_auth_user_depts = Table(
    "admin_auth_user_depts",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("admin_auth_user.id", ondelete="CASCADE")),
    Column("dept_id", Integer, ForeignKey("admin_auth_dept.id", ondelete="CASCADE")),
)

admin_auth_role_depts = Table(
    "admin_auth_role_depts",
    Base.metadata,
    Column("role_id", Integer, ForeignKey("admin_auth_role.id", ondelete="CASCADE")),
    Column("dept_id", Integer, ForeignKey("admin_auth_dept.id", ondelete="CASCADE")),
)

