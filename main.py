import contextvars
import logging
import uuid
from logging import LogRecord
import os
import time

from fastapi import FastAPI

import common

request_id = contextvars.ContextVar("request_id")


app = FastAPI()

# Setup Logger
class ContextInfo(logging.Filter):
    def __init__(self, request_id: str=None):
        self._request_id = request_id

    def filter(self, record: LogRecord) -> bool:
        record.request_id = self._request_id
        return True

logger = logging.getLogger('test-app')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)-12s: %(asctime)s - %(levelname)-8s - request_id: %(request_id)-15s - %(funcName)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

# On default behaviour, we don't set any message_id
# because we dont't have at the very begining
context_info = ContextInfo()
logger.addFilter(context_info)

logger.propagate = False


@app.get("/wait")
async def wait():
    print(os.getpid())
    request_id.set("wait_random_id")

    ranGenReqId = str(uuid.uuid4())
    context_info = ContextInfo(request_id=ranGenReqId)
    logger.addFilter(context_info)
    print("/wait ->", request_id.get())


    logger.info("Request comes from client to get long-waited resource access")
    await common.wait_longer()
    # time.sleep(10)
    logger.info("Request /wait completed successfully")
    print("/wait ->", request_id.get())
    return {"message": "I am come afer long wait"}


@app.get("/quick")
async def quick():
    print(os.getpid())
    request_id.set("quick_random_id")

    ranGenReqId = str(uuid.uuid4())
    context_info = ContextInfo(request_id=ranGenReqId)
    logger.addFilter(context_info)

    print("/quick ->", request_id.get())
    logger.info("Request comes from client to get quick resource access")
    common.quick()
    logger.info("Request /quick completed successfully")
    print("/quick ->", request_id.get())
    return {"message": "Quick response"}