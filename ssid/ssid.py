from abc import ABC, abstractmethod


class SSID(ABC):
    @abstractmethod
    def get_from_system(self) -> str:
        pass

    @abstractmethod
    def get_password(self, ssid: str) -> str:
        pass
