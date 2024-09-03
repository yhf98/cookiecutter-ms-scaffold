from sqlalchemy.orm import relationship, Mapped, mapped_column
from apps.platform.user.models import User
from db.db_base import BaseModel
from sqlalchemy import String, Integer, ForeignKey, Text, Float
from apps.admin.product.models.product import Product


class Usage(BaseModel):
    __tablename__ = "product_usage_record"
    __table_args__ = ({'comment': '产品使用统计表'})

    product_name: Mapped[str] = mapped_column(
        String(50), nullable=False, comment="API名称")

    response_time: Mapped[float] = mapped_column(
        Float, nullable=True, default=0.0, comment="响应时间")

    status: Mapped[int] = mapped_column(
        Integer, nullable=True, default=0, comment="状态，0：成功，1：失败")

    request_text: Mapped[str] = mapped_column(
        Text, nullable=True, comment="接口请求文本")

    response_text: Mapped[str] = mapped_column(
        Text, nullable=True, comment="接口响应文本")

    apikey: Mapped[str] = mapped_column(
        String(255), nullable=True, comment="API KEY")

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('user.id'), comment="用户ID")

    # user: Mapped['User'] = relationship("User", back_populates="usage")

    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('product.id'), comment="产品ID")

    # product: Mapped['Product'] = relationship("Product", back_populates="usage")
