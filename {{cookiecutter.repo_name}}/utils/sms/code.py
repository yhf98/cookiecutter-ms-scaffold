import datetime
import warnings
from redis.asyncio import Redis
from .aliyun import AliyunSMS
from core.logger import logger
from core.exception import CustomException


class CodeSMS(AliyunSMS):

    def __init__(self, phone: str, rd: Redis):
        super().__init__([phone], rd)

        self.phone = phone
        self.sign_conf = "sms_sign_name_1"
        self.template_code_conf = "sms_template_code_1"

    async def main_async(self) -> bool:
        """
        主程序入口，异步方式

        redis 对象必填
        """

        send_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if await self.rd.get(self.phone + "_flag_"):
            logger.error(f'{send_time} {self.phone} 短信发送失败，短信发送过于频繁')
            raise CustomException(msg="短信发送频繁", code=400)
        
        await self._get_settings_async()
        
        # # TODO: RELEASE🍛
        # result = await self._send_async(self.phone)
        # if not result:
        #     raise CustomException(msg="短信发送失败", code=500)
        
        # await self.rd.set(self.phone, self.code, self.valid_time)
        # await self.rd.set(self.phone + "_flag_", self.code, self.send_interval)
        
        # # FIXME: 调试模式🌻
        await self.rd.set(self.phone, "123456", self.valid_time)
        await self.rd.set(self.phone + "_flag_", "123456", self.send_interval)
        
        return True

    async def main(self) -> None:
        """
        主程序入口，同步方式
        """
        warnings.warn("此方法已废弃，如需要请重写该方法", DeprecationWarning)

    async def check_sms_code(self, code: str) -> bool:
        """
        检查短信验证码是否正确
        """
        if code and code == await self.rd.get(self.phone):
            await self.rd.delete(self.phone)
            await self.rd.delete(self.phone + "_flag_")
            return True
        return False

    def _get_template_param(self, **kwargs) -> str:
        """
        获取模板参数

        可以被子类继承的受保护的私有方法
        """
        self.code = kwargs.get("code", self.get_code())
        template_param = '{"code":"%s"}' % self.code
        return template_param

