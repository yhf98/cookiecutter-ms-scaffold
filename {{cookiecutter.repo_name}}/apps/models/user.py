from sqlalchemy.orm import  Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import String, Integer, DateTime, Text
from datetime import datetime

class User(BaseModel):
    __tablename__ = "user"
    __table_args__ = ({'comment': '用户信息表'})
    
    username: Mapped[str] = mapped_column(String(50), nullable=False, comment="用户名")
    username: Mapped[str] = mapped_column(String(255), nullable=False, comment="密码")
    age: Mapped[int] = mapped_column(Integer, nullable=True, comment="密码")
    