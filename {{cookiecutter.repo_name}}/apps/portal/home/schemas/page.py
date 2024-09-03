#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/08/01 13:51
# @File           : page.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from .question import QuestionOut


class Page(BaseModel):
    page_name: str | None = Field(None, title="page_name")
    title: str | None = Field(None, title="标题")
    question_id: str | None = Field(None, title="问题编号【1,2,3,4,5】")
    image: str | None = Field(None, title="落地页图片地址")
    


class PageSimpleOut(Page):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(..., title="创建时间")
    update_at: DatetimeStr = Field(..., title="更新时间")
    
class PageOut(Page):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    
    # questions: list[QuestionOut] = Field([], title="问题")
    question: QuestionOut | None = Field(None, title="问题-答案")
    
    create_at: DatetimeStr = Field(None, title="创建时间")
    update_at: DatetimeStr = Field(None, title="更新时间")
    
class PageDataOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sender: str | None = Field(None, title="sender", description= "标题")
    text: str | None = Field(None, title="sender", description= "文本")
