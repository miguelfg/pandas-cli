# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import click
import pandas as pd
import logging
# Why does this file exist, and why __main__?
# For more info, read:
# - https://www.python.org/dev/peps/pep-0338/
# - https://docs.python.org/2/using/cmdline.html#cmdoption-m
# - https://docs.python.org/3/using/cmdline.html#cmdoption-m

__author__ = 'miguelfg'


logger = logging.getLogger('pandas_cli')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(ch)


@click.command()
@click.argument('paths',
                type=click.Path(exists=True, dir_okay=True, file_okay=True, readable=True),
                nargs=-1,
                default=None)
def main(paths):
    """
    """
    for p in paths:
        df = pd.read_csv(p)
        click.echo(df.head(10))

if __name__ == "__main__":
    sys.exit(main())

