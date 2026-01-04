class RAGException(Exception):
    """
    Base exception class for:
    - unexpected code-breaking errors
    - pipeline/runtime failures
    - wrapping Python exceptions with context
    """

    def __init__(
        self,
        message: str,
        *,
        stage: str | None = None,
        retryable: bool = False,
        original_exception: Exception | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.stage = stage
        self.retryable = retryable
        self.original_exception = original_exception

    def to_dict(self) -> dict:
        """
        Structured representation for logging.
        """
        return {
            "error": self.message,
            "stage": self.stage,
            "retryable": self.retryable,
            "original_exception": (
                str(self.original_exception)
                if self.original_exception
                else None
            ),
        }

    def __str__(self) -> str:
        return self.message