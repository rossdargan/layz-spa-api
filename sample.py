import json
import getpass
from pprint import pprint
from pathlib import Path
from lazy_spa.auth import Auth
from lazy_spa.spa import Spa
from lazy_spa.errors import Error

def main():
    cache_file = Path("test_token.cache")

    if cache_file.is_file():
        response = json.loads(cache_file.read_text())
    else:
        try:
            email = input("Email Address: ")
            password = getpass.getpass("Password: ")
            auth = Auth()
            response = auth.get_token(email, password)
            cache_file.write_text(json.dumps(response))
        except  Error as authError:
            print ("Unable to authenticate: ", authError )
            return

    spa = Spa(response["data"]["api_token"], response["devices"][0]["did"])
    res2 = spa.status();
    print("current Temp", spa.temp_now);
    print ("Authentication Result: ", response["message"])


if __name__ == "__main__":
    main()