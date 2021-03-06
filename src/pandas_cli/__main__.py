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


class PDCLI():
    def __init__(self, cols, paths):
        """"""
        self.cols = cols
        self.paths = paths
        self.in_dfs = []
        self.out_dfs = []

    def read(self):
        """
        """
        click.echo("Reading input paths...")
        click.echo(self.paths)
        click.echo(self.cols)
        for path in self.paths:
            click.echo(path)
            self.in_dfs.append(pd.read_csv(path, usecols=self.cols))

    def echo(self):
        if self.out_dfs:
            pass
        else:
            for df in self.in_dfs:
                click.echo(df.head(10))

    def run(self):
        self.read()
        self.echo()


@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--cols', default=None, help='List of column names to use')
@click.argument('paths',
                type=click.Path(exists=True, dir_okay=True, file_okay=True, readable=True),
                default=None)
def main(ctx,   cols, paths):
    """
    """
    click.echo("################")
    click.echo("Show param values")
    click.echo("################")
    click.echo(cols)
    click.echo(paths)
    click.echo("################")
    click.echo("################")

    if isinstance(paths, (unicode, str, basestring)):
        paths = [paths]

    if cols:
        clean_cols = [col.strip() for col in cols.split(',')]
    else:
        clean_cols = None

    pd_cli = PDCLI(clean_cols, paths)
    pd_cli.run()


@click.command()
@click.pass_context
@click.option('--subset', default=None, help='Only consider certain columns for identifying duplicates, by default use all of the columns')
@click.option('--keep', default=None, help='{‘first’, ‘last’, False}, default ‘first’')
def drop_duplicates(ctx, subset, keep):
    """
    """
    click.echo("dropping dups!")


main.add_command(drop_duplicates)


if __name__ == "__main__":
    sys.exit(main())


# TODO: EXAMPLE OF DESIRED COMMAND LINES
# > pd <input_paths>
# > pd <input_paths> --cols a,b,c
# > pd <input_paths> --cols 1,3
# > pd <input_paths> --cols a,b,c --drop_duplicates all
# > pd <input_paths> --cols a,b,c --drop_duplicates b,c
# > pd <input_paths> --cols a,b,c --drop_duplicates b,c --drop_nas a,c
# > pd <input_paths> --cols a,b,c --filter a=10,b!='hello'
# > pd <input_paths> --cols a,b,c --filter d>=01/01/2016

# > pd.create 10x3
# > pd.create 10 --cols id,speed,mass -dt int,float,float
# > pd.create 10 --cols id,speed,mass -dt int,float,float <output_file>

# > pd.merge <input_paths>
# > pd <input_paths> --merge
# > pd <input_paths> --merge a

# > pd.concat <input_paths>

# > pd <input_paths> --groupby b
# > pd <input_paths> --groupby b,c

# > pd.left_join <input_paths>
# > pd.left_outer_join <input_paths>
# > pd.right_join <input_paths>
# > pd.right_outer_join <input_paths>
# > pd.full_join <input_paths>
# > pd.full_outer_join <input_paths>

# > pd <input_paths> --plot b,c --kind bar
# > pd <input_paths> --plot b,c --kind scatter

# > pd