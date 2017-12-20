# -*- coding: UTF-8 -*-

import logging
from config import SYS_LOG_PATH, SYS_LOG_LEVEL, DATA_LOG_PATH, DATA_LOG_LEVEL


def configure_logging():
    sys_handler = logging.handlers.WatchedFileHandler(SYS_LOG_PATH, encoding='utf-8')
    sys_formatter = logging.Formatter('%(asctime)s | %(funcName)s | %(levelname)s | %(message)s')
    sys_handler.setFormatter(sys_formatter)
    sys_logger = logging.getLogger('sys_log')
    sys_logger.setLevel(SYS_LOG_LEVEL)
    sys_logger.addHandler(sys_handler)

    data_handler = logging.handlers.WatchedFileHandler(DATA_LOG_PATH, encoding='utf-8')
    data_formatter = logging.Formatter('%(asctime)s | %(funcName)s | %(levelname)s | %(message)s')
    data_handler.setFormatter(data_formatter)
    data_logger = logging.getLogger('data_log')
    data_logger.setLevel(DATA_LOG_LEVEL)
    data_logger.addHandler(sys_handler)

    return sys_logger, data_logger


sys_logger, data_logger = configure_logging()
