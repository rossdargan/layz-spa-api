"""Authenticates with Lay-Z-Spa"""
import asyncio
from datetime import datetime
from .api import Api
class Spa:
    """The class to handle authenticating with the API"""
    def __init__(self, api, did):
        """
        constructor
        """
        self.api = Api({"did": did, "api_token":api})                  

    async def is_online(self):
        """
        Indicates if the device is currently online
        """
        result = await self.api.send_command("is_online")
        return result["data"] == "true"        

    async def update_status(self):        
        """
        Indicates if the device is currently online
        """
        result = await self.api.send_command("status")
        
        data = result["data"]                              
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

        self.power = attr["power"] == 1
        self.heat_power = attr["heat_power"] == 1
        self.wave_power = attr["wave_power"] == 1
        self.filter_power = attr["filter_power"] == 1

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

    async def set_power(self, power):
        """
        Turn the spa on or off
        """
        if power:
            await self.api.send_command("turn_on")
            power=True
        else:
            await self.api.send_command("turn_off")
            power=False

    async def set_filter_power(self, power):
        """
        Turn the filter on or off
        """
        if power:
            await self.api.send_command("turn_filter_on")
            filter_power=True
        else:
            await self.api.send_command("turn_filter_off")
            filter_power=False

    async def set_heat_power(self, power):
        """
        Turn the heater on or off
        """
        if power:
            await self.api.send_command("turn_heat_on")
            heat_power=True
        else:
            await self.api.send_command("turn_heat_off")
            heat_power=False

    async def set_wave_power(self, power):
        """
        Turn the bubbles on and off
        """
        if power:
            await self.api.send_command("turn_wave_on")
            wave_power=True
        else:
            await self.api.send_command("turn_wave_off")
            wave_power=False

    async def set_target_temperature(self, temperature):
        """
        Set the target temperature for the spa
        """
        await self.api.send_command("temp_set", {"temperature": temperature})
        target=temperature