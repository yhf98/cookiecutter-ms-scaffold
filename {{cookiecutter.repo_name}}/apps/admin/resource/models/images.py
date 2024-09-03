from sqlalchemy.orm import relationship, Mapped, mapped_column
from apps.admin.auth.models import AdminUser
from db.db_base import BaseModel
from sqlalchemy import String, ForeignKey, Integer

class AdminImages(BaseModel):
    __tablename__ = "admin_resource_images"
    __table_args__ = ({'comment': '图片素材表'})

    filename: Mapped[str] = mapped_column(String(255), nullable=False, comment="原图片名称")
    image_url: Mapped[str] = mapped_column(String(500), nullable=False, comment="图片链接")

    create_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_auth_user.id", ondelete='RESTRICT'),
        comment="创建人"
    )
    create_user: Mapped[AdminUser] = relationship(foreign_keys=create_user_id)
