class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidPasswordOrEmail(Error):
    """Raised when the API returns that the users password or email address is incorrect

    Attributes:
        message -- The error message
    """


    def __init__(self, message):
        self.message = message

class UnexpectedResponse(Error):
    """Raised when the API returns an unexpected response
    Attributes:
        message -- The error message
    """

    def __init__(self, message):
        self.message = message