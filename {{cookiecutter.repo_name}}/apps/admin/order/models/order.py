import random
from sqlalchemy import Integer, String, ForeignKey, DateTime, Float, func, DECIMAL
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.db_base import BaseModel
from apps.platform.user.models import User
from apps.admin.auth.models import AdminUser
from apps.admin.developer.models import Enterprise
from datetime import datetime
from decimal import Decimal as decimal
from apps.admin.product.models import Product


class Order(BaseModel):
    __tablename__ = 'order'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    order_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, comment='订单编号')
    order_type: Mapped[int] = mapped_column(Integer, nullable=False, comment='订单类型：0:充值，1:套餐，2:升级，3:续费')
    order_date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), comment='订单日期')
    total_amount: Mapped[decimal] = mapped_column(DECIMAL(18, 2), nullable=False, comment='订单总金额')
    status: Mapped[int] = mapped_column(Integer, default=0, comment='订单状态: 0:待支付，1:已支付，2:已取消，3:已退款，4:已关闭，5:已完成')
    recharge_method: Mapped[int] = mapped_column(Integer, default=0, comment='充值方式：0:微信支付，1:支付宝支付，2:余额支付，3:对公转账户，4:银行卡支付，5:其他支付方式')
    subjet_name: Mapped[str] = mapped_column(String(500), default=0, comment='账号主体名称')
    username: Mapped[str] = mapped_column(String(500), default=0, comment='用户账号')
    
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.id"),
        comment="用户ID"
    )
    user: Mapped[User] = relationship(foreign_keys=user_id)
    
    create_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_auth_user.id"),
        comment="创建人"
    )
    business_owners: Mapped[str] = mapped_column(String(500), comment='业务负责人')
    create_user: Mapped[AdminUser] = relationship(foreign_keys=create_user_id)
    
    # order_details: Mapped[list['OrderDetail']] = relationship('OrderDetail', back_populates='order')
    
    @staticmethod
    def generate_order_number(sequence: int = 1):
        date_str = datetime.now().strftime("%Y%m%d")
        random_sequence = random.randint(100000, 999999)
        order_number = f"ORD{date_str}{random_sequence:06d}{sequence:06d}"
        return order_number
    
class OrderDetail(BaseModel):
    __tablename__ = 'order_detail'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_name: Mapped[str] = mapped_column(String(500), nullable=False, comment='产品名称')
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, comment='数量')
    price: Mapped[decimal] = mapped_column(DECIMAL(18,5), nullable=False, comment='价格')
    preferential_price: Mapped[decimal] = mapped_column(DECIMAL(18,5), nullable=False, comment='优惠价')
    discount: Mapped[float] = mapped_column(Float, nullable=False, comment='折扣, 0.9表示9折')
    
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey('order.id'), nullable=False)
    # order: Mapped['Order'] = relationship('Order', back_populates='order_detail')
    
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'), comment="产品ID")
    # product: Mapped['Product'] = relationship("Product", back_populates="order_detail")