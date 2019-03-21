#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

import gi
import sys


def needver(namespace, version, apt_pkg):
    try:
        gi.require_version(namespace, version)
    except ValueError:
        sys.stderr.write('W: Failed to import ' + namespace + ' ' + version
            + '. You might need to install package ' + apt_pkg + '.\n')
