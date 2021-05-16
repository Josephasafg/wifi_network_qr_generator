import os
import sys
from shutil import which

from command_line_handler import CommandLineHandler
from ssid_getter.ssid import SSID


class LinuxSSID(SSID):
    def get_from_system(self) -> str:
        if which('nmcli') is None:
            raise ValueError('Network Manager is required to run this program on Linux')

        return CommandLineHandler.run_command("nmcli -t -f active,ssid dev wifi | egrep '^yes' | cut -d\: -f2") \
            .replace("\n", "")

    def get_password(self, ssid: str) -> str:
        if os.geteuid() != 0:
            raise OSError(f"You need to run '{sys.argv[0]}' as root")

        return CommandLineHandler.run_command(f"nmcli -s -g 802-11-wireless-security.psk connection show '{ssid}'") \
            .replace("\n", "")
