import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s %(asctime)s %(message)s')

counter = 0
while True:
    logger.info("My log message %d" % counter)
    counter += 1
    time.sleep(1)
