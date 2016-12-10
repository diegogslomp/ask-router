#!/usr/bin/env python

"""A script to get telnet command output from Enterasys routers/switches L3.
"""

from __future__ import print_function
from telnetlib import Telnet
import argparse
import sys


def get_telnet_output(ip, user, password, commands):

    tn = Telnet(ip)
    tn.read_until(b"Username:")
    tn.write(user.encode('ascii') + b"\n")
    tn.read_until(b"Password:")
    tn.write(password.encode('ascii') + b"\n")
    for command in commands:
        tn.write(command.encode('ascii') + b"\n")
    tn.write(b"exit\n")
    output = tn.read_all().decode('ascii')

    return output


def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-u', '--user', help='Telnet user', default='user')
    parser.add_argument('-p', '--password', help='Telnet password',
                        default='secret')
    parser.add_argument('ip', help='Ip address from target')
    parser.add_argument('commands', nargs='+', help='Telnet commands, separate \
                        with comma (,) if more than one')

    args = parser.parse_args(arguments)

    print(get_telnet_output(ip=args.ip, user=args.user, password=args.password,
          commands=' '.join(args.commands).split(',')))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
