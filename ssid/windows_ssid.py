import re

from command_line_handler import CommandLineHandler
from ssid_getter.ssid import SSID


class WindowsSSID(SSID):
    def get_from_system(self) -> str:
        ssid = CommandLineHandler.run_command("netsh wlan show interfaces | findstr SSID").replace("\r", "")

        if not ssid:
            raise ValueError('SSID not found')

        return re.findall(r"[^B]SSID\s+:\s(.*)", ssid)[0]

    def get_password(self, ssid: str) -> str:
        password = CommandLineHandler.run_command(f"netsh wlan show profile name=\"{ssid}\" key=clear | findstr Key") \
            .replace("\r", "")

        return re.findall(r"Key Content\s+:\s(.*)", password)[0]
