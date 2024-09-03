"""
类依赖项-官方文档：https://fastapi.tiangolo.com/zh/tutorial/dependencies/classes-as-dependencies/
"""
from fastapi import Depends
from core.dependencies import Paging, QueryParams


class DictDetailParams(QueryParams):
    """
    列表分页
    """
    def __init__(self, dict_type_id: int = None, label: str = None, params: Paging = Depends()):
        super().__init__(params)
        self.dict_type_id = dict_type_id
        self.label = ("like", label)
