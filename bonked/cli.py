#!/usr/bin/env python3
"""
Console script for bonked.
"""

from pathlib import Path
import sys
import click
try:
    from bonked import start_konch, logger, DBG, set_loguru, check_rc
except:
    from .bonked import start_konch, logger, DBG, set_loguru, check_rc

#DBG("bonked.cli")


def _validate_path(ctx, param, value):
    """This function is used if a file is specified to validate the path."""
    if value is None:
        return
    DBG(str(value))
    path = Path(value)
    if not check_rc(path):
        raise click.BadParameter('Must be an existing file '
                                 'or directory containing .konchrc file.')
    if path.is_dir():
        return path / '.konchrc'
    return path


@click.command(context_settings=dict(ignore_unknown_options=True, ))
@click.option(
    '-f',
    '--file',
    type=click.Path(exists=True,
                    file_okay=True,
                    dir_okay=True,
                    writable=False,
                    readable=True,
                    resolve_path=True,
                    allow_dash=False),
    default=None,
    callback=_validate_path,
    #multiple=True,
    help='Config file to use.')
@click.option('-d',
              '--debug',
              is_flag=True,
              default=False,
              help='Enable debug.')
@click.argument('konch_args', nargs=-1, type=click.UNPROCESSED)
def main(file, debug, konch_args):
    """Console script for bonked."""
    # See click documentation at http://click.pocoo.org/
    if debug:
        logger = set_loguru("DEBUG")
    DBG("bonked.cli.main")
    DBG(dir())
    DBG(file)
    if file is not None:
        DBG(str(file))
        file = Path(file)
    return start_konch(file, konch_args)


if __name__ == "__main__":
    DBG("bonked.cli, (__main__).")
    sys.exit(main())  # pragma: no cover
"""
# TODO:
    allow multiple files?
        ensure config and context updated, not over-written
    pass through konch commands
    http config file
    ptpython config
    ipython config
"""
