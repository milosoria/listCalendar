#!/usr/bin/env python3
import argparse
import sys
from typing import Any, Dict,Union

class Parser:

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
                "List incoming google calendar events and list them, ordered by date proximity"
                )
        self.setup()

    def setup(self) -> None:

        self.parser.add_argument('-n',
                '--number',
                help='Number of months to get events. Default 2',
                default=2,
                required=False)
        self.parser.add_argument(
                '-f',
                '--format',
                help=
                "\n- extension name to save the retreived events in a file with .extension\n- list, to get it as a list (default)",
                default='list',
                required=False)
        self.parser.add_argument(
                '-m',
                '--max',
                help="Maximum number of events to retrieve and display, default 10",
                default = 10,
                required=False)

    def handle_args(self) -> Union[Dict[str,Any], None]:
        args = vars(self.parser.parse_args())
        parsed_args = {}
        flags_errors = list()
        if args:
            try:
                args["number"] = int(args["number"])
            except ValueError:
                sys.stdout.write("Number of months entered is not a valid number\n")
                flags_errors.append("number")
            # except KeyError:

            try:
                args["max"] = int(args["max"])
            except ValueError:
                sys.stdout.write("Max number of events entered is not a valid number\n")
                flags_errors.append("max")

            if len(flags_errors) > 0:
                sys.stdout.write("Program exiting due to flag errors")
                exit(0)
            return args
