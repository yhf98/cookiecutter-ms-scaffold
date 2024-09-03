#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024/07/10 00:01
# @File           : interface_info.py
# @IDE            : VSCode
# @desc           : 接口信息

from fastapi import Depends
from pydantic import Field
from core.dependencies import Paging, QueryParams


class InterfaceInfoParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)
        
    name: str
