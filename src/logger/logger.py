import structlog
from typing import Optional


def get_logger(name: Optional[str] = None):
    """
    Get a structured logger.
    Safe to call from anywhere in the codebase.
    """
    return structlog.get_logger(name)