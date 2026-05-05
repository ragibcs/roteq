from roteq.custom_exception import InvalidURLException
from roteq.logger import logger

try:
    raise InvalidURLException()

except Exception as e:
    logger.error(f"An error occurred: {e}")
