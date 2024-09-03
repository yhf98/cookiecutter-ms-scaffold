"""
官方文档——中间件：https://fastapi.tiangolo.com/tutorial/middleware/
官方文档——高级中间件：https://fastapi.tiangolo.com/advanced/middleware/
"""
import datetime
import json
import time
import base64
import re
from fastapi import Request, Response
from core.logger import logger
from fastapi import FastAPI
from fastapi.routing import APIRoute
from user_agents import parse
from application.settings import OPERATION_RECORD_METHOD, MONGO_DB_ENABLE, IGNORE_OPERATION_FUNCTION, \
    DEMO_WHITE_LIST_PATH, DEMO, DEMO_BLACK_LIST_PATH
from utils.response import ErrorResponse
from apps.admin.record.crud import OperationRecordDal
from core.database import mongo_getter
from utils import status
from application import settings


def write_request_log(request: Request, response: Response):
    http_version = f"http/{request.scope['http_version']}"
    content_length = response.raw_headers[0][1]
    process_time = response.headers["X-Process-Time"]
    content = f"basehttp.log_message: '{request.method} {request.url} {http_version}' {response.status_code}" \
              f"{response.charset} {content_length} {process_time}"
    logger.info(content)
    
def parse_basic_auth(auth_header):
    """
    解析 Basic 认证头部信息，返回账号和密码
    :param auth_header: 授权头部信息，通常格式为 "Basic base64encodedstring"
    :return: (username, password) 元组
    """
    try:
        encoded_credentials = auth_header.strip().split(' ')[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        username, password = decoded_credentials.split(':')
        return username, password
    except Exception as e:
        print(e)
        return None, None


def register_request_log_middleware(app: FastAPI):
    """
    记录请求日志中间件
    :param app:
    :return:
    """

    @app.middleware("http")
    async def request_log_middleware(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        write_request_log(request, response)
        return response


def register_operation_record_middleware(app: FastAPI):
    """
    操作记录中间件
    用于将使用认证的操作全部记录到 mongodb 数据库中
    :param app:
    :return:
    """

    @app.middleware("http")
    async def operation_record_middleware(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        if not MONGO_DB_ENABLE:
            return response
        phone = request.scope.get('phone', None)
        user_id = request.scope.get('user_id', None)
        user_name = request.scope.get('user_name', None)
        route = request.scope.get('route')
        if not phone:
            return response
        elif request.method not in OPERATION_RECORD_METHOD:
            return response
        elif route.name in IGNORE_OPERATION_FUNCTION:
            return response
        process_time = time.time() - start_time
        user_agent = parse(request.headers.get("user-agent"))
        system = f"{user_agent.os.family} {user_agent.os.version_string}"
        browser = f"{user_agent.browser.family} {user_agent.browser.version_string}"
        query_params = dict(request.query_params.multi_items())
        path_params = request.path_params
        if isinstance(request.scope.get('body'), str):
            body = request.scope.get('body')
        else:
            body = request.scope.get('body').decode()
            if body:
                body = json.loads(body)
        params = {
            "body": body,
            "query_params": query_params if query_params else None,
            "path_params": path_params if path_params else None,
        }
        content_length = response.raw_headers[0][1]
        assert isinstance(route, APIRoute)
        document = {
            "process_time": process_time,
            "phone": phone,
            "user_id": user_id,
            "user_name": user_name,
            "request_api": request.url.__str__(),
            "client_ip": request.client.host,
            "system": system,
            "browser": browser,
            "request_method": request.method,
            "api_path": route.path,
            "summary": route.summary,
            "description": route.description,
            "tags": route.tags,
            "route_name": route.name,
            "status_code": response.status_code,
            "content_length": content_length,
            "create_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "params": json.dumps(params)
        }
        await OperationRecordDal(mongo_getter(request)).create_data(document)
        return response


def register_demo_env_middleware(app: FastAPI):
    """
    演示环境中间件
    :param app:
    :return:
    """

    @app.middleware("http")
    async def demo_env_middleware(request: Request, call_next):
        path = request.scope.get("path")
        if request.method != "GET":
            print("路由：", path, request.method)
        if DEMO and request.method != "GET":
            if path in DEMO_BLACK_LIST_PATH:
                return ErrorResponse(
                    status=status.HTTP_403_FORBIDDEN,
                    code=status.HTTP_403_FORBIDDEN,
                    msg="演示环境，禁止操作"
                )
            elif path not in DEMO_WHITE_LIST_PATH:
                return ErrorResponse(msg="演示环境，禁止操作")
        return await call_next(request)


def register_jwt_refresh_middleware(app: FastAPI):
    """
    JWT刷新中间件
    :param app:
    :return:
    """

    @app.middleware("http")
    async def jwt_refresh_middleware(request: Request, call_next):
        response = await call_next(request)
        refresh = request.scope.get('if-refresh', 0)
        response.headers["if-refresh"] = str(refresh)
        return response
def register_base_auth_middleware(app: FastAPI):
    """
    基础认证中间件
    :param app:
    :return:
    """
    @app.middleware("http")
    async def base_auth_middleware(request: Request, call_next):
        path = request.url.path
        query = request.url.query
        full_path = f"{path}?{query}" if query else path

        for exempt_path in settings.BASE_AUTH_WHITE_LIST_PATH:
            if re.match(exempt_path, full_path):
                response = await call_next(request)
                return response
        
        username, password = parse_basic_auth(request.headers.get("Authorization"))
        print("Auth base 账号密码：", username, password)
        
        if not username or not password:
            return ErrorResponse(
                    status=status.HTTP_401_UNAUTHORIZED,
                    code=status.HTTP_401_UNAUTHORIZED,
                    msg="请求没有用户名或密码"
                )
        
        if username != settings.AUTH_USER or password != settings.AUTH_PASSWORD:
            return ErrorResponse(
                    status=status.HTTP_403_FORBIDDEN,
                    code=status.HTTP_403_FORBIDDEN,
                    msg="用户名或密码错误"
                )
        response = await call_next(request)
        return response