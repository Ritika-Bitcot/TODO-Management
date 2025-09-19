# src/utils/exceptions.py
class ServiceError(Exception):
    """Base exception class for service layer errors."""

    def __init__(self, message: str, status_code: int = 400) -> None:
        """
        Initializes a ServiceError exception with a given message and status code.

        Args:
            message (str): The error message to be displayed.
            status_code (int, optional): The HTTP status code associated with this error. Defaults to 400.

        Returns:
            None
        """
        super().__init__(message)
        self.status_code = status_code
        self.message = message
