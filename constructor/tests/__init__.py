# (c) 2016 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# constructor is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

from __future__ import print_function, division, absolute_import

import sys

import constructor
from constructor.tests import test_parser


def main():
    print("sys.prefix: %s" % sys.prefix)
    print("sys.version: %s ..." % (sys.version[:40],))
    print('constructor version:', constructor.__version__)
    print('location:', constructor.__file__)

    if sys.platform == 'win32':
        import constructor.winexe as winexe
        winexe.read_nsi_tmpl()
    else:
        import constructor.shar as shar
        shar.read_header_template()

    test_parser.test_1()
    print("OK")


if __name__ == '__main__':
    main()