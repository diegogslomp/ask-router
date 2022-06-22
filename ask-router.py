#!/usr/bin/env python3
"""A script to run telnet commands on Enterasys routers/L3 switches
"""
from telnetlib import Telnet
import argparse
import sys


def run_telnet(ip: str, user: str, password: str, commands: list) -> str:
    with Telnet(ip) as tn:
        tn.read_until(b"Username:")
        tn.write(user.encode("ascii") + b"\n")
        tn.read_until(b"Password:")
        tn.write(password.encode("ascii") + b"\n")
        match_object = tn.expect([b"->", b"Username:"])[1]
        if match_object.group(0) == b"Username:":
            raise PermissionError("INVALID USER/PASSWORD")
        else:
            for command in commands:
                tn.write(command.encode("ascii") + b"\n")
            tn.write(b"exit\n")
            return tn.read_all().decode("ascii")


def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-u", "--user", help="Telnet user", default="root")
    parser.add_argument("-p", "--password", help="Telnet password", default="s3cr3t")
    parser.add_argument(
        "-F", "--field-separator", help="Telnet commands separator", default=","
    )
    parser.add_argument("ip", help="Ip address from target")
    parser.add_argument(
        "commands",
        nargs="+",
        help="Telnet commands separated with comma or custom --field-separator",
    )

    args = parser.parse_args(arguments)
    print(
        run_telnet(
            ip=args.ip,
            user=args.user,
            password=args.password,
            commands=" ".join(args.commands).split(args.field_separator),
        )
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
