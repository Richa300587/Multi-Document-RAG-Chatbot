from src.logger import configure_logging, get_logger
from src.exceptions import RAGException, RetrievalError

# 1️⃣ Configure logging ONCE
configure_logging()

logger = get_logger(__name__)

# 2️⃣ Normal log messages (use logger, not logging)
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

# 3️⃣ Simulate a code-breaking error
try:
    a = 1 + 'Z'   # ❌ TypeError

except Exception as e:
    # Log the error with full traceback
    logger.error(
        "code_execution_error",
        error="Error while running demo code",
        exc_info=True,   # 👈 file name, line number, traceback
    )

    # Wrap and re-raise using your custom exception
    raise RAGException(
        "Unexpected error during code execution",
        stage="runtime",
        retryable=False,
        original_exception=e,
    ) from e
