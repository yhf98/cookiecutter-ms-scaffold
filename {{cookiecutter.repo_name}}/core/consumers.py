import json
import asyncio
import threading
import time
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from core.database import get_db
from apps.admin.interface_info import models, schemas, crud as crud_interface
from utils.tools import get_current_time_zero
from core.rabbit_manage import RabbitMQ
from utils.tools import get_current_time_zero
from typing import Dict, Any

MAX_WORKERS = 1  # 最大工作线程数
async def process_message(message: Dict[str, Any]) -> bool:
    interface_info = json.loads(message['interface_info'])
    error_counter = int(message['error_counter'])
    success_counter = int(message['success_counter'])

    async with get_db() as db:
        interface_dal = crud_interface.InterfaceUsageDal(db)
        
        v_where = [
            models.InterfaceUsage.interface_id == 5,
            models.InterfaceUsage.enterprise_id == 1,
            models.InterfaceUsage.partition_date == get_current_time_zero()
        ]
        
        usage = await interface_dal.get_data_scales(v_where=v_where)
        if usage is None:
            create_data = schemas.InterfaceUsage(
                interface_id=interface_info['id'],
                interface_name=interface_info['name'],
                enterprise_id=1,
                enterprise_name="Aike",
                url=f"{interface_info['protocol']}://{interface_info['host']}:{interface_info['port']}/{interface_info['route_path']}",
                error_num=error_counter,
                success_num=success_counter,
                max_duration=5000,
                remaining_calls=100000,
                partition_date=get_current_time_zero(),
            )
            await interface_dal.create_data(create_data)
        else:
            usage.error_num += error_counter
            usage.success_num += success_counter
            await interface_dal.put_data(usage.id, usage)
        
        await db.commit()
        
    return True
    
async def process_message_wrapper(ch, method, properties, body):
    message = json.loads(body)
    if await process_message(message):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("消息处理成功：")
    else:
        print("消息处理失败")
        ch.basic_nack(delivery_tag=method.delivery_tag)
        
def on_message_callback(ch, method, properties, body):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(process_message_wrapper(ch, method, properties, body))
    loop.close()
    
def on_message_callback(ch, method, properties, body, loop):
    asyncio.run_coroutine_threadsafe(process_message_wrapper(ch, method, properties, body), loop)

def start_consumer(loop):
    rabbitmq = RabbitMQ()
    rabbitmq.consume_messages(lambda ch, method, properties, body: on_message_callback(ch, method, properties, body, loop), loop)

def start_consumer_new_thread(loop):
    print("启动MQ消费者线程")
    consumer_thread = threading.Thread(target=start_consumer, args=(loop,))
    consumer_thread.start()