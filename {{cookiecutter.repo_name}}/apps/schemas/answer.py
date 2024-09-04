#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/08/01 13:52
# @File           : answer.py
# @IDE            : VSCode
# @desc           : pydantic 模型，用于数据库序列化操作

from pydantic import BaseModel, Field, ConfigDict
from core.data_types import DatetimeStr


class Answer(BaseModel):
    title: str | None = Field(None, title="答案标题")
    content: str | None = Field(None, title="答案内容")


class AnswerSimpleOut(Answer):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(0, title="编号")
