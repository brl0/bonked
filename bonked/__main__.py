#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" This is the entry point for if your module is
executed like this: ``python -m bonked``. """

import sys
try:
    from .cli import main
except:
    from cli import *

#DBG("bonked.__main__.py.")

if __name__ == '__main__':
    #DBG("bonked.__main__.py, (__main__).")
    sys.exit(main())  # pragma: no cover
