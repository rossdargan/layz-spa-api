"""Authenticates with Lay-Z-Spa"""
import requests
import json
from datetime import datetime
from .const import (
    API_URI,
    API_VERSION
)
class Spa:
    """The class to handle authenticating with the API"""
    def __init__(self, api, did):
        """
        constructor
        """
        self.api = api
        self.did = did

    def is_online(self):
        """
        Indicates if the device is currently online
        """
        data = {"did": self.did, "api_token":self.api}
        r = requests.post(API_URI + "/v" + API_VERSION + "/gizwits/is_online", data=data)
        if r.status_code == 200:
            return r.json()["data"] == "true"
        return r

    def status(self):
        """
        Indicates if the device is currently online
        """
        data = {"did": self.did, "api_token":self.api}
        r = requests.post(API_URI + "/v" + API_VERSION + "/gizwits/status", data=data)
        if r.status_code == 200:
            data= r.json()["data"]
            print(data);            
            self.updated_at = datetime.fromtimestamp(data["updated_at"])
            attr = data["attr"]
            
            self.wave_appm_min = attr["wave_appm_min"]
            self.heat_timer_min = attr["heat_timer_min"]
            self.earth = attr["earth"]
            self.wave_timer_min = attr["wave_timer_min"]

            self.filter_timer_min = attr["filter_timer_min"]
            self.heat_appm_min = attr["heat_appm_min"]
            self.filter_appm_min = attr["filter_appm_min"]

            self.locked = attr["locked"]

            self.power = attr["power"]
            self.heat_power = attr["heat_power"]
            self.wave_power = attr["wave_power"]
            self.filter_power = attr["filter_power"]

            self.temp_now = attr["temp_now"]
            self.temp_set = attr["temp_set"]
            self.temp_set_unit ="°C" if attr["temp_set_unit"]=="摄氏" else "°F"
            self.heat_temp_reach = attr["heat_temp_reach"] == 1



            self.system_err1 = attr["system_err1"]
            self.system_err2 = attr["system_err2"]
            self.system_err3 = attr["system_err3"]
            self.system_err4 = attr["system_err4"]
            self.system_err5 = attr["system_err5"]
            self.system_err6 = attr["system_err6"]
            self.system_err7 = attr["system_err7"]
            self.system_err8 = attr["system_err8"]
            self.system_err9 = attr["system_err9"]

            
            
        return r