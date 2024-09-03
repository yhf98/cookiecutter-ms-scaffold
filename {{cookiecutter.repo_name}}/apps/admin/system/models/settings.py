from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import String, Integer, ForeignKey, Boolean, Text

class AdminSystemSettingsTab(BaseModel):
    __tablename__ = "admin_system_settings_tab"
    __table_args__ = ({'comment': '系统配置分类表'})

    title: Mapped[str] = mapped_column(String(255), comment="标题")
    classify: Mapped[str] = mapped_column(String(255), index=True, nullable=False, comment="分类键")
    tab_label: Mapped[str] = mapped_column(String(255), comment="tab标题")
    tab_name: Mapped[str] = mapped_column(String(255), index=True, nullable=False, unique=True, comment="tab标识符")
    hidden: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否隐藏")
    disabled: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否禁用")

    settings: Mapped[list["AdminSystemSettings"]] = relationship(back_populates="tab")


class AdminSystemSettings(BaseModel):
    __tablename__ = "admin_system_settings"
    __table_args__ = ({'comment': '系统配置表'})

    config_label: Mapped[str] = mapped_column(String(255), comment="配置表标签")
    config_key: Mapped[str] = mapped_column(String(255), index=True, nullable=False, unique=True, comment="配置表键")
    config_value: Mapped[str | None] = mapped_column(Text, comment="配置表内容")
    remark: Mapped[str | None] = mapped_column(String(255), comment="备注信息")
    disabled: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否禁用")

    tab_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_system_settings_tab.id", ondelete='CASCADE'),
        comment="关联tab标签"
    )
    tab: Mapped[AdminSystemSettingsTab] = relationship(foreign_keys=tab_id, back_populates="settings")
