import logging
import asyncio
import time

# logger = logging.getLogger('test-app')

async def wait_longer(log_object):
    log_object.info('Starting long process')
    await asyncio.sleep(10)
    return None

def quick(log_object):
    log_object.info('Starting quick process')
    return None
