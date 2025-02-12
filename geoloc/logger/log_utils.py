import logging
import os
import sys
from logging.handlers import RotatingFileHandler


class LogUtils:
    log_level_map = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
    }

    def __init__(self, file_name):
        self.log_file_name = file_name
        self.log_format = "%(asctime)s | %(levelname)-5s | %(funcName)-45s:%(lineno)-5d | %(message)s"
        self.ensure_log_directory_exists()
        self.logger = logging.getLogger(__name__)
        self.configure_logger()

    def ensure_log_directory_exists(self):
        log_dir = os.path.dirname(self.log_file_name)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def configure_logger(self):
        self.logger.handlers = []
        self.logger.propagate = False

        # if not root_logger.handlers:  # Avoid adding multiple handlers if already configured
        formatter = logging.Formatter(self.log_format, datefmt='%Y-%m-%d %H:%M:%S')

        # Console handler
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.CRITICAL)
        stream_handler.setFormatter(formatter)

        # Create a file handler
        file_handler = RotatingFileHandler(self.log_file_name)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        root_logger = logging.getLogger()
        root_logger.handlers = []
        root_logger.addHandler(stream_handler)
        root_logger.addHandler(file_handler)
        root_logger.setLevel(logging.DEBUG)

    def get_logger(self):
        return self.logger
