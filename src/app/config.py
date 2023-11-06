import logging
import os
import uuid

from dotenv import load_dotenv
from pygelf import GelfUdpHandler

load_dotenv()
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


# Создадим класс с методом filter, который будет подставлять reuqest_id в каждую запись
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.request_id = str(uuid.uuid4())
        return True


logger = logging.getLogger('just_logger')
logger.setLevel(logging.INFO)
graylog_host = os.getenv("GRAYLOG_HOST")
graylog_port_udp = os.getenv("GRAYLOG_PORT_UDP")
if graylog_host and graylog_port_udp:
    handler = GelfUdpHandler(host=graylog_host, port=int(graylog_port_udp), include_extra_fields=True)
    logger.addHandler(handler)
    logger.addFilter(ContextFilter())

