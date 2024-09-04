import datetime
import random
import re
import string
import secrets
import pytz
from typing import List, Union
import importlib
from core.logger import logger
from typing import Any
from decimal import Decimal


def test_password(password: str) -> Union[str, bool]:
    """
    检测密码强度
    """
    if len(password) < 8 or len(password) > 16:
        return '长度需为8-16个字符,请重新输入。'
    else:
        for i in password:
            if 0x4e00 <= ord(i) <= 0x9fa5 or ord(i) == 0x20:  # Ox4e00等十六进制数分别为中文字符和空格的Unicode编码
                return '不能使用空格、中文，请重新输入。'
        else:
            key = 0
            key += 1 if bool(re.search(r'\d', password)) else 0
            key += 1 if bool(re.search(r'[A-Za-z]', password)) else 0
            key += 1 if bool(re.search(r"\W", password)) else 0
            if key >= 2:
                return True
            else:
                return '至少含数字/字母/字符2种组合，请重新输入。'


def list_dict_find(options: List[dict], key: str, value: any) -> Union[dict, None]:
    """
    字典列表查找
    """
    return next((item for item in options if item.get(key) == value), None)


def get_time_interval(start_time: str, end_time: str, interval: int, time_format: str = "%H:%M:%S") -> List:
    """
    获取时间间隔
    :param end_time: 结束时间
    :param start_time: 开始时间
    :param interval: 间隔时间（分）
    :param time_format: 字符串格式化，默认：%H:%M:%S
    """
    if start_time.count(":") == 1:
        start_time = f"{start_time}:00"
    if end_time.count(":") == 1:
        end_time = f"{end_time}:00"
    start_time = datetime.datetime.strptime(start_time, "%H:%M:%S")
    end_time = datetime.datetime.strptime(end_time, "%H:%M:%S")
    time_range = []
    while end_time > start_time:
        time_range.append(start_time.strftime(time_format))
        start_time = start_time + datetime.timedelta(minutes=interval)
    return time_range

def get_current_time(time_format: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    获取当前时间
    :param time_format: 字符串格式化，默认：%Y-%m-%d %H:%M:%S
    """
    return datetime.datetime.now().strftime(time_format)

def get_current_time_stamp(time_format: str = "%Y-%m-%d %H:%M:%S") -> int:
    """
    获取当前时间戳
    :param time_format: 字符串格式化，默认：%Y-%m-%d %H:%M:%S
    """
    return int(datetime.datetime.strptime(get_current_time(time_format), time_format).timestamp())

def get_current_date(time_format: str = "%Y-%m-%d") -> str:
    """
    获取当前日期
    :param time_format: 字符串格式化，默认：%Y-%m-%d
    """
    return datetime.datetime.now().strftime(time_format)

def get_current_time_zero() -> datetime:
    """
    获取当前日期的时间戳，时间设为00:00:00。
    :param time_format: 字符串格式化，默认为年-月-日（%Y-%m-%d 00:00:00）
    """
    current_date = datetime.datetime.now()
    return current_date.replace(hour=0, minute=0, second=0, microsecond=0)

def generate_string(length: int = 8) -> str:
    """
    生成随机字符串
     """
    return ''.join(random.sample(string.ascii_letters + string.digits, length))

def generate_apikey(length=48):
    """
    API KEY 生成    
    :param length: 生成apikey长度
    """
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))

def import_modules(modules: list, desc: str, **kwargs):
    for module in modules:
        if not module:
            continue
        try:
            # 动态导入模块
            module_pag = importlib.import_module(module[0:module.rindex(".")])
            getattr(module_pag, module[module.rindex(".") + 1:])(**kwargs)
        except ModuleNotFoundError:
            logger.error(f"AttributeError：导入{desc}失败，未找到该模块：{module}")
        except AttributeError:
            logger.error(f"ModuleNotFoundError：导入{desc}失败，未找到该模块下的方法：{module}")


async def import_modules_async(modules: list, desc: str, **kwargs):
    for module in modules:
        if not module:
            continue
        try:
            # 动态导入模块
            module_pag = importlib.import_module(module[0:module.rindex(".")])
            await getattr(module_pag, module[module.rindex(".") + 1:])(**kwargs)
        # except TimeoutError:
        #     logger.error(f"asyncio.exceptions.TimeoutError：连接Mysql数据库超时")
        #     print(f"asyncio.exceptions.TimeoutError：连接Mysql数据库超时")
        except ModuleNotFoundError:
            logger.error(f"AttributeError：导入{desc}失败，未找到该模块：{module}")
        except AttributeError:
            logger.error(f"ModuleNotFoundError：导入{desc}失败，未找到该模块下的方法：{module}")


def convert_decimal_to_str(data: Any) -> Any:
    if isinstance(data, list):
        return [convert_decimal_to_str(item) for item in data]
    if isinstance(data, dict):
        return {key: convert_decimal_to_str(value) for key, value in data.items()}
    if isinstance(data, Decimal):
        return str(data)
    return data

def convert_decimal_to_float(data: Any) -> Any:
    if isinstance(data, list):
        return [convert_decimal_to_float(item) for item in data]
    if isinstance(data, dict):
        return {key: convert_decimal_to_float(value) for key, value in data.items()}
    if isinstance(data, Decimal):
        return float(data)
    return data

def expire_time_seconds(target_date: datetime.datetime) -> int:
    """
    计算当前日期与目标日期的时间差（以秒为单位），确保考虑东八区时区。
    :param target_date: 目标日期，预期已经是东八区时区的 datetime 对象
    :return: 时间差（秒）
    """
    eastern_eight_timezone = pytz.timezone('Asia/Shanghai')
    
    now = datetime.datetime.now(eastern_eight_timezone)
    
    if target_date.tzinfo is None or target_date.tzinfo.utcoffset(target_date) is None:
        target_date = eastern_eight_timezone.localize(target_date)
    
    return int((target_date - now).total_seconds())

def get_current_datetime_utc():
    """
    获取当前东八区时间
    """
    eastern_eight_timezone = pytz.timezone('Asia/Shanghai')
    
    return datetime.datetime.now(eastern_eight_timezone)

def mark_apikey_str(apikey) -> str:
    """
    隐藏apikey
    """
    return f"{apikey[:4]}******{apikey[-4:]}"