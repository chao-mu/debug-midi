#!/usr/bin/env python3

#
# Install directions:
# pip3 install mido python-rtmidi
#

# Standard library
import re
import time
import sys
import os.path
import argparse
import time

# Community
import mido

def main():
    parser = argparse.ArgumentParser(prog="debug-midi.py", description="Debug midi devices")
    subparsers = parser.add_subparsers(help="commands", dest="command")
    parser_list = subparsers.add_parser("list", help="List midi ports")
    parser_dump = subparsers.add_parser("dump", help="dump midi messages")

    parser_dump.add_argument("--name", required=True,
            help="The input port name, get this from the list command")
    parser_dump.add_argument("--skip-clock", default=False,
            action='store_true',
            help="Skip clock messages")

    args = parser.parse_args()

    cmd = args.command
    if cmd == "list":
        cmd_list()
    elif cmd == "dump":
        cmd_dump(args.name, args.skip_clock)

def cmd_list():
    input_names = mido.get_input_names()
    print("Input Ports (readable)")
    for name in input_names:
        print("    {}".format(name))

    print()

    output_names = mido.get_output_names()
    print("Output Ports (writable)")
    for name in output_names:
        print("    {}".format(name))

def cmd_dump(name, skip_clock):
    names = mido.get_input_names()
    if name not in names:
        print("Error! '{}' not a present input port".format(name))
        return

    port = mido.open_input(name)

    print("Listening on '{}'. ctrl-c to exit".format(name))
    while True:
        while port.poll():
            pass

        for msg in port:
            if not skip_clock or msg.type != "clock":
                print("{:1.7f} {}".format(time.time(), repr(msg)))

if __name__ == "__main__":
    main()
