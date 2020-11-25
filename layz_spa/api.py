import json
import aiohttp
import asyncio
from datetime import datetime
from .const import (
    API_URI,
    API_VERSION
)
from .errors import InvalidPasswordOrEmail, UnexpectedResponse
class Api:
    """The class to handle communicating with the api"""
    def __init__(self, auth, base_url=API_URI + "/v" + API_VERSION + "/gizwits/"):
        """
        constructor
        """
        self.auth = auth
        self.base_url = base_url

    async def send_command(self, command, query_string={}):       
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url+command, data=self.auth,params=query_string) as r:         
                       
                if r.status == 200:
                    return await r.json()
                if r.status == 403:
                    raise InvalidPasswordOrEmail((await r.json())["errors"])        
                r.raise_for_status()
                raise UnexpectedResponse(await r.text())                
