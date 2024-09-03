from datetime import datetime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import Integer, String, Boolean, DateTime, func, ForeignKey
from apps.admin.auth.models.user import AdminUser

class ApplyUser(BaseModel):
    __tablename__ = "apply_user"
    __table_args__ = ({'comment': '申请用户列表'})
    
    username: Mapped[str | None] = mapped_column(String(255), comment='用户名称')
    phone: Mapped[str] = mapped_column(String(20), nullable=False, index=True, comment="手机号", unique=False)
    apply_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='申请时间')
    intention_product: Mapped[datetime] = mapped_column(String(500), nullable=True, comment='意向产品')
    contact_name: Mapped[str] = mapped_column(String(255), nullable=False, comment='联系人姓名')
    contact_phone: Mapped[str] = mapped_column(String(500), nullable=False, comment='联系人电话')
    organize: Mapped[str] = mapped_column(String(500), nullable=False, comment='组织名称')
    status: Mapped[int] = mapped_column(Integer, nullable=False, default=0, comment='跟进状态：0-未跟进，1-已跟进')
    
    create_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_auth_user.id"),
        comment="创建人[跟进人]"  
    )
    create_user: Mapped[AdminUser] = relationship(foreign_keys=create_user_id)