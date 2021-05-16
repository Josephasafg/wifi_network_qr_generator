import qrcode


class QRCode:
    @classmethod
    def generate(cls, ssid: str, password: str, with_image: bool = True):
        network_config = cls._network_text_config(ssid=ssid, password=password)

        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=10,
                           border=4)

        qr.add_data(network_config)

        if with_image:
            return cls._save_qr_to_image(qr=qr, ssid=ssid)

        return cls._qr_to_tty(qr)

    @classmethod
    def _network_text_config(cls, ssid: str, password: str) -> str:
        # Source: https://git.io/JtLIv
        return f'WIFI:T:WPA;S:{ssid};P:{password};;'

    @classmethod
    def _save_qr_to_image(cls, qr: qrcode.QRCode, ssid: str) -> None:
        file_name = ssid.replace(' ', '_') + '.png'
        qr_image = qr.make_image()
        qr_image.save(file_name)

    @classmethod
    def _qr_to_tty(cls, qr: qrcode.QRCode) -> None:
        qr.make()
        qr.print_ascii()
