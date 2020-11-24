"""Authenticates with Lay-Z-Spa"""
import requests
from .errors import InvalidPasswordOrEmail, UnexpectedResponse

class Auth:
    """The class to handle authenticating with the API"""

    def __init__(self):
        """
        constructor
        """

    def get_token(self, email, password):
        """
        Gets an authentication token for the user
        :type email: str
        :type password: str
        """
        r = requests.post("https://mobileapi.lay-z-spa.co.uk/v1/auth/login", data={"email": email, "password":password})
        if r.status_code == 200:
            return r.json()
        if r.status_code == 403:
            raise InvalidPasswordOrEmail(r.json()["errors"])        
        
        raise UnexpectedResponse(r.json()["errors"])