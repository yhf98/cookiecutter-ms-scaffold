
from sqlalchemy.orm import relationship, Mapped, mapped_column
from apps.admin.auth.models import AdminUser
from db.db_base import BaseModel
from sqlalchemy import String, Integer, ForeignKey, Text, Float, DateTime, func
from apps.admin.developer.models import Enterprise
from .interface_info import InterfaceInfo
from datetime import datetime


class InterfaceUsage(BaseModel):
    __tablename__ = "interface_usage"
    __table_args__ = ({'comment': '接口用量统计表'})

    interface_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("interface_info.id"),
        comment="接口ID"
    )
    interface_info: Mapped[InterfaceInfo] = relationship(
        foreign_keys=interface_id)
    interface_name: Mapped[str] = mapped_column(
        String(500), nullable=True, comment="接口名称")
    enterprise_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("enterprise.id"),
        comment="企业ID"
    )
    enterprise: Mapped[Enterprise] = relationship(foreign_keys=enterprise_id)
    enterprise_name: Mapped[str] = mapped_column(
        String(500), nullable=True, comment="企业名称")
    url: Mapped[str] = mapped_column(
        String(500), nullable=True, comment="接口地址")
    error_num: Mapped[int] = mapped_column(
        Integer, nullable=True, default=0, comment="错误次数")
    success_num: Mapped[int] = mapped_column(
        Integer, nullable=True, default=0, comment="成功次数")
    max_duration: Mapped[float] = mapped_column(
        Float, nullable=True, default=0.0, comment="最长耗时")
    remaining_calls: Mapped[int] = mapped_column(
        Integer, nullable=True, default=0, comment="剩余调用量")
    partition_date: Mapped[datetime] = mapped_column(
        DateTime, index=True, nullable=False, default=None, comment='分区时间')

    def __repr__(self) -> str:
        return f"id:{self.id},interface_id:{self.interface_id},interface_name:{self.interface_name},enterprise_id:{self.enterprise_id},enterprise_name:{self.enterprise_name},url:{self.url},error_num:{self.error_num},success_num:{self.success_num},max_duration:{self.max_duration},remaining_calls:{self.remaining_calls},partition_date:{self.partition_date},create_at:{self.create_at},update_at:{self.update_at},delete_datetime:{self.delete_datetime},is_delete:{self.is_delete}"
