
from sqlalchemy.orm import relationship, Mapped, mapped_column
from apps.admin.auth.models import AdminUser
from db.db_base import BaseModel
from sqlalchemy import String, Integer, ForeignKey, Text, Boolean

class InterfaceInfo(BaseModel):
    __tablename__ = "interface_info"
    __table_args__ = ({'comment': '接口信息表'})

    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="接口名称")
    description: Mapped[str] = mapped_column(String(500), index=True, nullable=False, comment="接口描述")
    host: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="接口主机、IP")
    protocol: Mapped[str] = mapped_column(String(20), index=True, nullable=False, comment="协议:http、https")
    method: Mapped[str] = mapped_column(String(20), index=True, nullable=False, comment="请求方式：GET、POST、PUT、DELETE")
    port: Mapped[int] = mapped_column(Integer, nullable=False, default=80, comment="端口：1-65536")
    
    path: Mapped[str] = mapped_column(String(500), nullable=True, comment="服务根路径：/api/v1/ai")
    
    route_path: Mapped[str] = mapped_column(String(500), nullable=False, comment="网关路由地址：/tts")
    request_params: Mapped[str] = mapped_column(Text, nullable=False, comment="请求参数")
    request_header: Mapped[str] = mapped_column(Text, nullable=False, comment="请求头")
    response_header: Mapped[str] = mapped_column(Text,nullable=False, comment="响应头")
    status: Mapped[str] = mapped_column(Integer, index=True, nullable=False, default=0, comment="状态，0：开启，1：关闭")
    is_free: Mapped[bool] = mapped_column(Boolean, default=False, comment="是否是免费的接口，0：否，1：是")
    
    create_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("admin_auth_user.id", ondelete='RESTRICT'),
        comment="创建人"
    )
    create_user: Mapped[AdminUser] = relationship(foreign_keys=create_user_id)