#!/usr/bin/env python3
from listcalendar.lister import Lister
from listcalendar.parser import Parser

def main():
    parser = Parser()
    args = parser.handle_args()
    lister = Lister(args["number"],args["format"])
    service = lister.authenticate()
    lister.call_api(service)
    lister.write_events()

if __name__ == "__main__":
    main()
