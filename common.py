import logging
import time

logger = logging.getLogger('test-app')

def wait_longer():
    logger.info('Starting long process')
    time.sleep(10)
    return None

def quick():
    logger.info('Starting quick process')
    return None
