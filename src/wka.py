#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

import gi
# gi.require_version('Gtk', '3.10')
# Gtk 3 docs: https://python-gtk-3-tutorial.readthedocs.io/en/latest/
# gi.require_version('WebKit', '2.4')

from gi.repository import Gtk, WebKit

import os
import sys

import cfg_core
import cfg_misc
import cfg_window_geometry


class WebKitApp():

    def __init__(self, cfg):
        self.cfg = cfg
        self.versions = {
            'gtk': (Gtk.get_major_version(), Gtk.get_minor_version(),
                    Gtk.get_micro_version(),),
            'webkit': (WebKit.major_version(), WebKit.minor_version(),
                        WebKit.micro_version(),)
            }

        appwin = Gtk.Window()
        # ^- API: https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Window.html
        self.appwin = appwin
        appwin.set_default_size(750, 550)
        scrollpane = Gtk.ScrolledWindow()
        appwin.add(scrollpane)
        appframe = WebKit.WebView()
        self.appframe = appframe
        scrollpane.add(appframe)

        cfg_misc.title_pattern(cfg.str('title'), appwin, appframe)
        cfg.str('icon', hook=appwin.set_icon_from_file)
        cfg_window_geometry.apply(appwin, cfg)

        appwin.show_all()


    def run(self):
        cfg = self.cfg
        cfg.str('cwd', hook=os.chdir)
        self.appframe.open(cfg.str('url', 'http://localhost/'))
        appwin = self.appwin
        appwin.connect('destroy', Gtk.main_quit)
        Gtk.main()














if __name__ == '__main__':
    WebKitApp(
        cfg=cfg_core.WkaCfg(
            env='wka_',
            cli_args=sys.argv,
            ),
        ).run()
