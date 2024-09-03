#!/usr/bin/python
# -*- coding: utf-8 -*-
# @version        : 1.0
# @Create Time    : 2024-07-29 22:05:23
# @File           : crud.py
# @IDE            : VSCode
# @desc           :
from core.crud import DalBase
from . import models, schemas
from sqlalchemy.ext.asyncio import AsyncSession


class DataPageDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(DataPageDal, self).__init__()
        self.db = db
        self.model = models.DataPage
        self.schema = schemas.DataPageSimpleOut


class PageDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(PageDal, self).__init__()
        self.db = db
        self.model = models.Page
        self.schema = schemas.PageSimpleOut


class QuestionDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(QuestionDal, self).__init__()
        self.db = db
        self.model = models.Question
        self.schema = schemas.QuestionSimpleOut


class AnswerDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(AnswerDal, self).__init__()
        self.db = db
        self.model = models.Answer
        self.schema = schemas.AnswerSimpleOut
