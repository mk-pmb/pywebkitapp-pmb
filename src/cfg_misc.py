#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-

def title_pattern(pattern, appwin, appframe):
    slot = ''
    if pattern:
        slot = pattern[0:1]
        pattern = pattern[1:]
    use_slot = (pattern and slot and (slot in pattern))
    if not use_slot:
        appwin.set_title(pattern)
        return
    def on_document_title_changed(widget, frame, title):
        title = pattern.replace(slot, title)
        appwin.set_title(title)
    on_document_title_changed(None, None, '')
    appframe.connect('title-changed', on_document_title_changed)


def decide_useragent(cfg):
    ua = cfg.str('useragent')
    if ua: return ua
    ua = ' '.join([
        'Mozilla/5.0',
        '(Windows NT 6.1; Win64; x64)',
        'AppleWebKit/538.15',
        '(KHTML, like Gecko)',
        'Version/8.0',
        (cfg.pkgmeta['name'] + '/' + cfg.pkgmeta['version']),
        ])
    return ua


def webkitview(frame, cfg):
    sett = frame.get_settings()
    sett.set_property('user-agent', decide_useragent(cfg))

    return frame
