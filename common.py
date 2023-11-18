import logging
import asyncio


logger = logging.getLogger('test-app')

async def wait_longer():
    logger.info('[INFO] Starting long process...')
    await asyncio.sleep(10)
    return None

def quick():
    logger.info('[INFO] Starting quick process¡...')
    return None
