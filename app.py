import logging
import time

from pythonjsonlogger import jsonlogger

logger = logging.getLogger(__name__)

handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.basicConfig(handlers=(handler,), level=logging.INFO)

counter = 0
while True:
    message = {
        "counter": counter,
        "field_one": "field one content",
        "field_two": "field two content"
    }

    logger.info(message)
    counter += 1
    time.sleep(1)
