import os
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler
from from_root import from_root
import structlog


LOG_DIR = "logs"
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 3


def configure_logging():
    """
    Configure DEBUG-level structured logging.
    Must be called ONCE at application startup.
    """

    log_dir_path = os.path.join(from_root(), LOG_DIR)
    os.makedirs(log_dir_path, exist_ok=True)

    log_file_path = os.path.join(
        log_dir_path,
        f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers (FastAPI reload safety)
    if root_logger.handlers:
        return

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        log_file_path,
        maxBytes=MAX_LOG_SIZE,
        backupCount=BACKUP_COUNT,
    )
    file_handler.setLevel(logging.DEBUG)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    # Structlog configuration
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.EventRenamer("event"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG),
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
