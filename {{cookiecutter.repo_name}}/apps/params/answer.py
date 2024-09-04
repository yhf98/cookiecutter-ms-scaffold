#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/08/01 13:52
# @File           : answer.py
# @IDE            : VSCode
# @desc           : 答案

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class AnswerParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
