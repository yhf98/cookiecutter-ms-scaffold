#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/09/04 13:57
# @File           : user.py
# @IDE            : VSCode
# @desc           : 用户

from fastapi import Depends
from core.dependencies import Paging, QueryParams


class UserParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
