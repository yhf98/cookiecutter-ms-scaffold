from sqlalchemy.orm import  Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import String, Integer, DateTime, Text
from datetime import datetime

class DataPage(BaseModel):
    __tablename__ = "data_page"
    __table_args__ = ({'comment': '落地页数据表'})
    
    title: Mapped[str] = mapped_column(Text, nullable=True, comment="标题")
    describe: Mapped[str] = mapped_column(Text, nullable=True, comment="描述")