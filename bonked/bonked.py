#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main module."""

import sys
import typing
from pathlib import Path
#import logging
from loguru import logger

LOG_LEVEL = "DEBUG"

# Disable logging, may be changed by options
r"""
bllb_path = r'C:\Users\b_r_l\OneDrive\Documents\code\python\bllb'
bllb_path = str(Path(bllb_path).resolve())
sys.path.insert(0, bllb_path)
from bllb_logging import setup_logging, DBG
logger = setup_logging(enable=True,
                       lvl=LOG_LEVEL,
                       std_lib=False,
                       loguru_enqueue=True)
"""

DBG = logger.debug


def set_loguru(lvl):
    """Reset loguru log level by removing and adding back."""
    logger.remove()
    logger.add(
        sys.stdout,
        level=lvl,
        colorize=True,
        format=
        '<green>{time:HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>',
        enqueue=True)
    return logger


logger = set_loguru(LOG_LEVEL)

#DBG("bonked.py")


def check_rc(d: typing.Union[Path, str]) -> bool:
    path = Path(d)
    if path.is_dir():
        path = path / '.konchrc'
    return path.is_file()


def find_rc_file(rc: typing.Union[Path, None] = None
                 ) -> typing.Union[Path, None]:
    """Find '.konchrc' file.
    Search order: optional path, current directory, home.
    """
    name = ".konchrc"
    paths = list()
    if rc is not None:
        paths.append(rc)
    paths.extend([Path(name), Path.home() / name])
    file = None
    DBG(f'Searching for rc in paths:\n{paths}')
    for path in paths:
        if path.exists():
            DBG('Config file found.')
            file = path
            break
    DBG(file)
    return file


def start_konch(rc: typing.Union[Path, None] = None,
                konch_args: typing.Union[typing.Sequence[typing.Any], None] = None) -> None:
    """Start konch, optionally specify rc file."""
    rc = find_rc_file(rc)
    import konch
    konch.logger = logger
    if rc is None:
        logger.info('Config file not found.')
        konch.main(konch_args)
    else:
        konchrc = konch.use_file(rc)
        DBG(dir(konchrc))
        DBG(f'{dir(konchrc.konch)}')
        DBG(f'konch_args: {konch_args}')
        konch.start(konch_args)
    return


if __name__ == '__main__':
    from cli import main
    #DBG("bonked, (__main__)")
    sys.exit(main())  # pragma: no cover
"""
# TODO:
    tmux integration?
    conemu integration? (env)
"""
