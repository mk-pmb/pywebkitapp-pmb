#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

import re


def parse(geom):
    # Gtk's parse_geometry() is deprecated, and also we have extra features.
    nums = re.split('([+-])', geom, 4) + (['+', ''] * 4)
    def to_signed_int(sign, num):
        if num:
            num = sign + num
            if num == '-0': return num
            return int(num)
        return None
    size = list(zip(['width', 'height'],
            [to_signed_int('', n) for n in nums[0].split('x')[:2]] + [None]))
    posi = list(zip(['left', 'top', 'addLeft', 'addTop'],
            [to_signed_int(s, n) for s, n in zip(nums[1::2], nums[2::2])]))
    geom = dict(size + posi)
    return geom


def pos_int_or(x, d):
    if x == '-0': return d
    if x is None: return d
    x = int(x)
    if x > 0: return x
    return d


def apply(win, cfg):
    wmc_appname = cfg.str('winname', 'WebKitAppPmb')
    wmc_wincls = cfg.str('wincls', 'AppWin')
    # Reminder which is which: `wmctrl -xl` displays appname.wincls
    win.set_wmclass(wmc_appname, wmc_wincls)

    geom = parse(cfg.str('geometry'))
    width = pos_int_or(geom['width'], 750)
    height = pos_int_or(geom['height'], 550)
    win.set_default_size(width, height)

    def neg_geom_posi(pos, add, size, max):
        pos = geom[pos]
        if pos is None:
            return -1
        if pos == '-0':
            pos = max - size
        elif pos < 0:
            pos += max
        add = geom[add]
        if add: pos += int(add)
        return pos
    screen = win.get_screen()
    left = neg_geom_posi('left', 'addLeft', width, screen.get_width())
    top = neg_geom_posi('top', 'addTop', height, screen.get_height())
    win.move(left, top)

    allow_resize = True
    win.set_has_resize_grip(allow_resize)
    win.set_resizable(allow_resize)

    win.set_decorated(True)














