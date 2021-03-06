import json
import getpass
from pprint import pprint
from pathlib import Path
import asyncio
from layz_spa.auth import Auth
from layz_spa.spa import Spa
from layz_spa.errors import Error
async def main():
    cache_file = Path("test_token.cache")

    if cache_file.is_file():
        response = json.loads(cache_file.read_text())
    else:
        try:
            email = input("Email Address: ")
            password = getpass.getpass("Password: ")
            auth = Auth()
            response = await auth.get_token(email, password)
            cache_file.write_text(json.dumps(response))
        except  Error as authError:
            print ("Unable to authenticate: ", authError )
            return

    spa = Spa(response["data"]["api_token"], response["devices"][0]["did"])
    
    print(await spa.is_online())
    await spa.update_status()
    print("current power", spa.temp_set)    

    await spa.set_power(True)
    print("current power 1", spa.power)    

 

   # await spa.set_power(True)
    print("current power 2", spa.power)    

    await spa.set_target_temperature(22)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())