"""
类依赖项-官方文档：https://fastapi.tiangolo.com/zh/tutorial/dependencies/classes-as-dependencies/
"""
from fastapi import Depends
from core.dependencies import Paging, QueryParams


class LoginParams(QueryParams):
    """
    列表分页
    """
    def __init__(
            self,
            ip: str = None,
            address: str = None,
            phone: str = None,
            status: bool = None,
            platform: str = None,
            params: Paging = Depends()
    ):
        super().__init__(params)
        self.ip = ("like", ip)
        self.phone = ("like", phone)
        self.address = ("like", address)
        self.status = status
        self.platform = platform
        self.v_order = "desc"
