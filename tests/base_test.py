import pytest

from geoloc.logger.log_utils import LogUtils


class BaseTest:
    log_utils = LogUtils(file_name="logs/geo-loc-tests.log")
    logger = log_utils.get_logger()