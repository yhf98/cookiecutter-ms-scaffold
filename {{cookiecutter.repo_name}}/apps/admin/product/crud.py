#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-26 15:45:18
# @File           : crud.py
# @IDE            : VSCode
# @desc           :
from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase
from . import models, schemas
from sqlalchemy.orm import joinedload


class ProductDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(ProductDal, self).__init__()
        self.db = db
        self.model = models.Product
        self.schema = schemas.ProductSimpleOut


class ProductTypeDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(ProductTypeDal, self).__init__()
        self.db = db
        self.model = models.ProductType
        self.schema = schemas.ProductTypeSimpleOut
        
    async def get_type_products(self) -> dict:
        """
        获取每个分类下的所有产品
        """
        data = {}
        options = [joinedload(self.model.products)]
        objs = await ProductTypeDal(self.db).get_datas(
            limit=0,
            v_return_objs=True,
            v_options=options,
        )
        for obj in objs:
            if not obj:
                data[obj.type_name] = []
            else:
                data["id"] = obj.id
                data["type_name"] = obj.type_name
                data["description"] = obj.description
                data["products"] = [schemas.ProductSimpleOut.model_validate(i).model_dump() for i in obj.products]
                # TODO: 获取用户是否购买过🧂
                data["is_buy"] = False
                data["is_try"] = False
        return data
