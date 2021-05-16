#!/usr/bin/env python3

import argparse
import sys

from .qr import QRCode
from .ssid import create_ssid


def print_error(text: str) -> None:
    print(f"ERROR: {text}")
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(usage='%(prog)s [options]')
    parser.add_argument('--qrcode', "-q", action="store_true", default=True, help="Generate a QR code")
    parser.add_argument('--image', "-i", action="store_true", dest='image', default=False,
                        help="Create the QR code as image instead of showing it on the terminal "
                             "(must be used along with --qrcode)")

    parser.add_argument('--ssid', "-s", default=create_ssid(),
                        help="Specify a SSID that you have previously connected to")
    parser.add_argument('--password', type=str, help='Password to match the given SSID provided')

    args = parser.parse_args()

    # Don't get creds from system
    if args.password and args.ssid:
        QRCode.generate(ssid=args.ssid, password=args.password, with_image=args.image)
        return

    ssid = args.ssid.get_from_system()
    password = args.ssid.get_password(ssid)

    if args.qrcode:
        args.no_password = True
        QRCode.generate(ssid=ssid, password=password, with_image=args.image)
        return


if __name__ == "__main__":
    main()
