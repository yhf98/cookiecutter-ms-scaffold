from sqlalchemy.orm import  Mapped, mapped_column
from db.db_base import BaseModel
from sqlalchemy import String, Text

class Page(BaseModel):
    __tablename__ = "page"
    __table_args__ = ({'comment': '落地页'})
    
    page_name: Mapped[str] = mapped_column(String(5000), nullable=True, comment="page_name")
    title: Mapped[str] = mapped_column(String(5000), nullable=True, comment="标题")
    question_id: Mapped[str] = mapped_column(String(500), nullable=True, comment="问题编号【1,2,3,4,5】")
    image: Mapped[str] = mapped_column(String(500), nullable=True, comment="落地页图片地址")
    
    
class Question(BaseModel):
    __tablename__ = "question"
    __table_args__ = ({'comment': '问题'})
    
    question: Mapped[str] = mapped_column(Text, nullable=True, comment="问题")
    sub_question: Mapped[str] = mapped_column(Text, nullable=True, comment="子问题")
    answer: Mapped[str] = mapped_column(Text, nullable=True, comment="答案")
    
class Answer(BaseModel):
    __tablename__ = "answer"
    __table_args__ = ({'comment': '答案'})
    
    title: Mapped[str] = mapped_column(Text, nullable=True, comment="答案标题")
    content: Mapped[str] = mapped_column(Text, nullable=True, comment="答案内容")