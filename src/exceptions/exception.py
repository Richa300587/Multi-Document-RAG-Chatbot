from .base import RAGException


class RetrievalError(RAGException):
    """
    Raised when document retrieval confidence is too low
    or retrieval fails semantically.
    """
    pass


class EmbeddingError(RAGException):
    """
    Raised when embedding generation fails.
    """
    pass


class LLMCallError(RAGException):
    """
    Raised when an LLM call fails or times out.
    """
    pass
