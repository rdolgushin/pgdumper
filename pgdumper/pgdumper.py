#!/usr/bin/env python

from mydumper.mydumper import Dumper;

def main():
    dumper = Dumper(
        "Simple PostgreSQL dumper.",
        "pg_dump -U %(user)s -h %(host)s %(db)s > %(dump_file)s", False
    )
    dumper.run()
