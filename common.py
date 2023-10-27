import logging
import asyncio
import time

logger = logging.getLogger('test-app')

async def wait_longer():
    logger.info('Starting long process')
    await asyncio.sleep(10)
    return None

def quick():
    logger.info('Starting quick process')
    return None
