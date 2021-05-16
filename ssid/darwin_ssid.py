import sys
from pathlib import Path

from command_line_handler import CommandLineHandler
from .ssid import SSID


class DarwinSSID(SSID):
    def get_from_system(self) -> str:
        airport = Path('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport')

        if not airport.is_file():
            print(f"Can't find 'airport' command at {airport}")
            sys.exit(1)

        return CommandLineHandler.run_command(f"{airport} -I | awk '/ SSID/ {{print substr($0, index($0, $2))}}'") \
            .replace("\n", "")

    def get_password(self, ssid: str) -> str:
        return CommandLineHandler. \
            run_command(f"security find-generic-password -l \"{ssid}\" -D 'AirPort network password' -w") \
            .replace("\n", "")
