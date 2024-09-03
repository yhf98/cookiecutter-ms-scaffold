"""
类依赖项-官方文档：https://fastapi.tiangolo.com/zh/tutorial/dependencies/classes-as-dependencies/
"""
from fastapi import Depends
from core.dependencies import Paging, QueryParams


class SMSParams(QueryParams):
    """
    列表分页
    """
    def __init__(self, phone: str = None, params: Paging = Depends()):
        super().__init__(params)
        self.phone = ("like", phone)
