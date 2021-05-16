import sys
from enum import Enum

from .darwin_ssid import DarwinSSID
from .linux_ssid import LinuxSSID
from .ssid import SSID
from .windows_ssid import WindowsSSID


class SSIDType(Enum):
    Darwin = 'darwin'
    Windows = 'win32'
    Linux = 'linux'


def create_ssid() -> SSID:
    if sys.platform == SSIDType.Darwin.value:
        return DarwinSSID()

    if sys.platform == SSIDType.Linux.value:
        return LinuxSSID()

    if sys.platform == SSIDType.Windows.value:
        return WindowsSSID()

    raise ValueError(f'Type of OS: {sys.platform} is not supported')
