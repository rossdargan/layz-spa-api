"""Authenticates with Lay-Z-Spa"""
from .api import Api
from .const import (
    API_URI,
    API_VERSION
)
class Auth:
    """The class to handle authenticating with the API"""

    def __init__(self):
        """
        constructor
        """

    async def get_token(self, email, password):
        """
        Gets an authentication token for the user
        :type email: str
        :type password: str
        """
        api = Api({"email": email, "password":password}, base_url=API_URI + "/v" + API_VERSION )
        return await api.send_command("/auth/login")