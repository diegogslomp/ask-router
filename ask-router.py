#!/usr/bin/env python
"""A script to get telnet command output from Enterasys routers/switches L3.
"""
from telnetlib import Telnet
import argparse
import sys


def get_telnet_output(ip: str, user: str, password: str, commands: list) -> str:
    output = ""
    try:
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
                output = tn.read_all().decode("ascii")
    except Exception as exc:
        output = f"ERRO: {exc}"
    finally:
        return output


def main(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("-u", "--user", help="Telnet user", default="user")
    parser.add_argument("-p", "--password", help="Telnet password", default="secret")
    parser.add_argument(
        "-F", "--field-separator", help="Telnet commands separator", default=","
    )
    parser.add_argument("ip", help="Ip address from target")
    parser.add_argument(
        "commands",
        nargs="+",
        help="Telnet commands, separate \
                        with comma (or custom --field-separator) if more than one",
    )

    args = parser.parse_args(arguments)
    print(
        get_telnet_output(
            ip=args.ip,
            user=args.user,
            password=args.password,
            commands=" ".join(args.commands).split(args.field_separator),
        )
    )


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
