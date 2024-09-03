from sqlalchemy.orm import relationship, Mapped, mapped_column
from apps.admin.auth.models import AdminUser
from db.db_base import BaseModel
from sqlalchemy import String, Integer, ForeignKey, Text, Boolean,DECIMAL
from decimal import Decimal as decimal

class ProductType(BaseModel):
    __tablename__ = "product_type"
    __table_args__ = ({'comment': '产品类型表'})

    type_name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="产品类型名称")
    description: Mapped[str] = mapped_column(Text, nullable=True, comment="产品类型描述")
    order: Mapped[int] = mapped_column(Integer, nullable=True, default=0, comment="排序：0-9999999，越大越靠前")
    
    products: Mapped[list["Product"]] = relationship("Product", back_populates="product_type")
    
class Product(BaseModel):
    __tablename__ = "product"
    __table_args__ = ({'comment': '产品信息表'})
    
    api_id: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="APIID")
    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="产品名称")
    description: Mapped[str] = mapped_column(Text, nullable=True, comment="描述")
    versions: Mapped[str] = mapped_column(String(50), nullable=True, comment="版本，接口版本号")
    accounting_method: Mapped[int] = mapped_column(Integer, nullable=True, default=0, comment="核算方式，0：流量包扣费，1：单次扣费，···")
    billing_plan: Mapped[str] = mapped_column(Integer, nullable=True, comment="计费方案···")
    price: Mapped[decimal] = mapped_column(DECIMAL(18, 5), nullable=True, comment="单价：0.01元/次")
    order: Mapped[int] = mapped_column(Integer, nullable=True, default=0, comment="排序：0-9999999，越大越靠前")
    # 服务配置信息
    docs_url: Mapped[str] = mapped_column(String(500), nullable=True, comment="接口文档地址")
    serve_name: Mapped[str] = mapped_column(String(500), unique=True, nullable=False, comment="服务名称")
    host: Mapped[str] = mapped_column(String(50), nullable=False, comment="接口主机、IP")
    protocol: Mapped[str] = mapped_column(String(20), nullable=False, default="http", comment="协议:http、https")
    method: Mapped[str] = mapped_column(String(20), nullable=False, default="GET", comment="请求方式：GET、POST、PUT、DELETE")
    port: Mapped[int] = mapped_column(Integer, nullable=False, default=80, comment="端口：1-65536")
    path: Mapped[str] = mapped_column(String(500), nullable=True, comment="服务根路径：/api/v1/ai")
    route_path: Mapped[str] = mapped_column(String(500), nullable=True, comment="网关路由地址：/tts")
    request_params: Mapped[str] = mapped_column(Text, nullable=True, comment="请求参数")
    request_header: Mapped[str] = mapped_column(Text, nullable=True, comment="请求头")
    response_header: Mapped[str] = mapped_column(Text,nullable=True, comment="响应头")
    status: Mapped[int] = mapped_column(Integer, nullable=True, default=0, comment="状态，0：开启，1：关闭，2：其他")
    is_free: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否是免费的接口，0：否，1：是")
    limit_of_seconds: Mapped[int] = mapped_column(Integer, nullable=True, default=5, comment="每秒可以发出的 HTTP 请求量")
    limit_of_minutes: Mapped[int] = mapped_column(Integer, nullable=True, default=300, comment="每分钟可以发出的 HTTP 请求量")
    product_type_id: Mapped[int] = mapped_column(Integer, ForeignKey('product_type.id'), comment="产品类型ID")
    product_type: Mapped[ProductType] = relationship("ProductType", back_populates="products")
    
    create_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_auth_user.id", ondelete='CASCADE'),
        comment="创建人"
    )
    create_user: Mapped[AdminUser] = relationship(foreign_keys=create_user_id)
    
