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

