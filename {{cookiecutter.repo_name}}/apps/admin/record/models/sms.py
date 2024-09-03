from sqlalchemy.orm import Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import Integer, String, Boolean, ForeignKey

class AdminSMSSendRecord(BaseModel):
    __tablename__ = "admin_record_sms_send"
    __table_args__ = ({'comment': '短信发送记录表'})

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("admin_auth_user.id", ondelete='CASCADE'), comment="操作人")
    status: Mapped[bool] = mapped_column(Boolean, default=True, comment="发送状态")
    content: Mapped[str] = mapped_column(String(255), comment="发送内容")
    phone: Mapped[str] = mapped_column(String(11), comment="目标手机号")
    desc: Mapped[str | None] = mapped_column(String(255), comment="失败描述")
    scene: Mapped[str | None] = mapped_column(String(50), comment="发送场景")
