#!/usr/bin/env python

import os
import sys

BASE_DIR = os.path.dirname(__file__)
FLVREC_EXECUTABLE_SYSTEM = os.path.join(sys.prefix, 'lib/flvrec')
FLVREC_EXECUTABLE_LOCAL = os.path.join(BASE_DIR, 'lib/flvrec')
FLVREC_EXECUTABLE = (
    FLVREC_EXECUTABLE_SYSTEM if os.path.exists(
        FLVREC_EXECUTABLE_SYSTEM)
    else FLVREC_EXECUTABLE_LOCAL
)


def main():
    args = [] if len(sys.argv) < 2 else sys.argv[1:]
    os.execv(FLVREC_EXECUTABLE, [FLVREC_EXECUTABLE] + args)


if __name__ == '__main__':
    main()
