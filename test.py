import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
import skrf as rf
logger.info(f"skrf version: {rf.__version__}")