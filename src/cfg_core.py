#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

import os


def makePrefixedGetEnv(prefix):
    return lambda key: os.getenv(prefix + key, '')


class WkaCfg():

    def __init__(self, env, cli_args=None):
        if isinstance(env, str):
            env = makePrefixedGetEnv(env)
        self._env = env

    def str(self, key, dflt='', hook=None):
        val = self._env(key)
        if not val: return dflt
        if hook: hook(val)
        return val

