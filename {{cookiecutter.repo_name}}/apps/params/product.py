from fastapi import Depends
from core.dependencies import Paging, QueryParams


class ProductParams(QueryParams):
    def __init__(self, params: Paging = Depends()):
        super().__init__(params)