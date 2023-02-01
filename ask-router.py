"""A script to run telnet commands on Enterasys routers/L3 switches
"""
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from telnetlib import Telnet
import sys
import os


def run_telnet(ip: str, user: str, password: str, commands: list) -> str:
    with Telnet(ip) as tn:
        tn.read_until(b"Username:")
        tn.write(user.encode("ascii") + b"\n")
        tn.read_until(b"Password:")
        tn.write(password.encode("ascii") + b"\n")
        match_object = tn.expect([b"->", b"Username:"])[1]
        if match_object.group(0) == b"Username:":
            raise PermissionError("INVALID USER/PASSWORD")
        for command in commands:
            tn.write(command.encode("ascii") + b"\n")
        tn.write(b"exit\n")
        return tn.read_all().decode("ascii")


def parse_args(arguments: list[str]) -> list[str]:
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    user = os.getenv("TELNET_USER", "root")
    password = os.getenv("TELNET_PASS", "s3cr3t")
    parser.add_argument("-u", "--user", help="Telnet user", default=user)
    parser.add_argument("-p", "--password", help="Telnet password", default=password)
    parser.add_argument(
        "-F", "--field-separator", help="Telnet commands separator", default=","
    )
    parser.add_argument("ip", help="Ip address from target")
    parser.add_argument(
        "commands",
        nargs="+",
        help="Telnet commands separated with comma or custom --field-separator",
    )
    return parser.parse_args(arguments)


def main(arguments: list) -> None:
    args = parse_args(arguments)
    commands = " ".join(args.commands).split(args.field_separator)
    output = run_telnet(
        ip=args.ip,
        user=args.user,
        password=args.password,
        commands=commands,
    )
    print(output)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
