from sqlalchemy.orm import relationship, Mapped, mapped_column
from apps.admin.auth.models import AdminUser
from db.db_base import BaseModel
from sqlalchemy import String, Integer, ForeignKey
from apps.platform.user.models import User

class Enterprise(BaseModel):
    __tablename__ = "enterprise"
    __table_args__ = ({'comment': '企业开发者'})
    
    enterprise_name: Mapped[str] = mapped_column(String(255), index=True, unique=True, nullable=False, comment="企业名称")
    phone: Mapped[str] = mapped_column(String(20), index=True, unique=True, nullable=False, comment="手机号码")
    legal_name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="法人姓名")
    legal_id_number: Mapped[str] = mapped_column(String(20), index=True, nullable=False, comment="法人身份证号")
    business_license: Mapped[str] = mapped_column(String(500), nullable=False, comment="营业执照")
    social_credit_code: Mapped[str] = mapped_column(String(50), nullable=False, comment="统一社会信用代码")
    status: Mapped[str] = mapped_column(Integer, index=True, nullable=False, default=0, comment="状态，0：正常，1：冻结")
    address: Mapped[str] = mapped_column(String(500), nullable=True, comment="地址")
    other_phone: Mapped[str] = mapped_column(String(20), nullable=True, comment="其他联系电话")
    email: Mapped[str] = mapped_column(String(50), nullable=True, comment="邮箱")
    industry: Mapped[str] = mapped_column(String(50), nullable=True, comment="行业")
    
    # user_id: Mapped[int] = mapped_column(
    #     Integer,
    #     ForeignKey("user.id"),
    #     comment="用户ID"
    # )
    
    # user: Mapped[User] = relationship(foreign_keys=user_id)
    
    create_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_auth_user.id", ondelete='RESTRICT'),
        comment="创建人"
    )
    create_user: Mapped[AdminUser] = relationship(foreign_keys=create_user_id)
    
    