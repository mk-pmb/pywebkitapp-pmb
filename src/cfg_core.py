#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

import os

from os.path import realpath, dirname, join as joinpath, exists as fexists
from codecs import open as cfopen

from json import load as load_json_from_filepointer


def make_prefixed_getenv(prefix):
    return lambda key: os.getenv(prefix + key, '')


def read_json_file(fn):
    with cfopen(fn, encoding='UTF-8') as fp:
        return load_json_from_filepointer(fp)


pkgdir = dirname(dirname(__file__))
pkgmeta = read_json_file(joinpath(pkgdir, 'package.json'))


class WkaCfg():

    def __init__(self, env, cli_args=None):
        if isinstance(env, str):
            env = make_prefixed_getenv(env)
        self._env = env
        self.pkgdir = pkgdir
        self.pkgmeta = pkgmeta

    def str(self, key, dflt='', hook=None):
        val = self._env(key)
        if not val: return dflt
        if hook: hook(val)
        return val

