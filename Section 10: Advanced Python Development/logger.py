"""
Logging - levels

DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename="logs.txt"
)
logger = logging.getLogger(__name__)

logger.info("Only shows if level=INFO or below")
logger.warning("This always shows")

