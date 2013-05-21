Simple PostgreSQL dumper
========================

Pgdumper allows you:

* To make dumps of PostgreSQL databases
* Automaticaly remove outdated or unnecessary of stored dumps

Installation
------------

> Is recommended to install pgdumper with [pip](http://www.pip-installer.org) and [virtualenv](http://www.virtualenv.org/), but you can also use any other [method](http://wiki.python.org/moin/CheeseShopTutorial) of Python package installing.

### From PyPI

    $ pip install pgdumper

### From Git sources

    $ git clone git://github.com/rdolgushin/pgdumper.git
    $ pip install -e pgdumper/

Usage
-----

    $ pgdumper
    usage: pgdumper -u USER [-h HOST] -d DUMP_DIR
                    [-m MAX_DUMPS_QTY] [-M MAX_DAYS_DELTA]
                    database
    $ pgdumper -u john -p secret -m 10 -M 3 test_db

Crontab example:

    0 */1 * * * * /home/john/.virtualenvs/default/bin/pgdumper -u john -m 10 -M 3 test_db

See also
--------

* [Mydumper](https://github.com/rdolgushin/mydumper)
