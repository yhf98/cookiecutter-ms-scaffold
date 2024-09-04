import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from core.database import Base

config = context.config

fileConfig(config.config_file_name)

# 添加当前项目路径到环境变量
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 导入项目中的基本映射类，与 需要迁移的 ORM 模型
# from apps.admin.auth.models import *
# from apps.admin.system.models import *
# from apps.admin.record.models import *
# from apps.admin.help.models import *
# from apps.admin.resource.models import *
# from apps.admin.interface_info.models import *
# # from apps.admin.developer.models import *
# from apps.platform.user.models import *
# from apps.platform.apikey.models import *
# from apps.admin.order.models import *
# from apps.admin.product.models import *
# from apps.platform.apply.models import *
# from apps.admin.usage.models import *
from apps.models import *

# 修改配置中的参数
target_metadata = Base.metadata

def run_migrations_offline():
    """
    以“脱机”模式运行迁移。
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,  # 是否检查字段类型，字段长度
        compare_server_default=True  # 是否比较在数据库中的默认值
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    以“在线”模式运行迁移。
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # 是否检查字段类型，字段长度
            compare_server_default=True  # 是否比较在数据库中的默认值
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    print("offline")
    run_migrations_offline()
else:
    print("online")
    run_migrations_online()