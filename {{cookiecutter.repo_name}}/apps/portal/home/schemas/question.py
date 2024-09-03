#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/08/01 13:52
# @File           : question.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr
from .answer import AnswerSimpleOut

class Question(BaseModel):
    question: str | None = Field(None, title="问题")
    sub_question: str | None = Field(None, title="子问题")
    answer: str | None = Field(None, title="答案")


class QuestionSimpleOut(Question):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title="编号")
    create_at: DatetimeStr = Field(None, title="创建时间")
    update_at: DatetimeStr = Field(None, title="更新时间")
    
class QuestionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(0, title="编号")
    question: str | None = Field(None, title="问题")
    answer: str | None = Field(None, title="答案")
    
    # answers: list[AnswerSimpleOut] = Field([], title="答案")
    
