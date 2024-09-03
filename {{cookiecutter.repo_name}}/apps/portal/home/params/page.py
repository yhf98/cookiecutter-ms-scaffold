#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/08/01 13:51
# @File           : page.py
# @IDE            : VSCode
# @desc           : 落地页

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class PageParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
