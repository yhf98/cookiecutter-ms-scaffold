from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import DalBase
from . import models, schemas

class IssueDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(IssueDal, self).__init__()
        self.db = db
        self.model = models.AdminIssue
        self.schema = schemas.IssueSimpleOut

    async def add_view_number(self, data_id: int) -> None:
        """
        更新常见问题查看次数+1
        """
        obj: models.AdminIssue = await self.get_data(data_id)
        obj.view_number = obj.view_number + 1 if obj.view_number else 1
        await self.flush(obj)


class IssueCategoryDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(IssueCategoryDal, self).__init__()
        self.db = db
        self.model = models.AdminIssueCategory
        self.schema = schemas.IssueCategorySimpleOut
