#!/bin/bash
# -*- coding: utf-8, tab-width: 2 -*-


function wka_rocket_chat () {
  export LANG{,UAGE}=en_US.UTF-8  # make error messages search engine-friendly
  local SELFPATH="$(readlink -m "$BASH_SOURCE"/..)"
  cd -- "$SELFPATH" || return $?

  local APP_HOME="$HOME/.wka/$FUNCNAME"
  # ^-- avoid cluttering your home directory directly with the caches and stuff.
  mkdir --parents -- "$APP_HOME" || return $?

  local WKA_ENV=(
    HOME="$APP_HOME"
    wka_url='https://open.rocket.chat/'
    wka_cwd=/
    wka_icon='/usr/share/icons/Humanity/categories/48/applications-chat.svg'
    wka_wincls="$FUNCNAME"
    # wka_winname=pywebkitapp
    wka_title='%Rocket Chat Open Demo: %'
    )
  # exec &>"$APP_HOME"/debug.log || return $?
  exec env "${WKA_ENV[@]}" ../../bin/pywebkitapp-pmb
}


wka_rocket_chat "$@"; exit $?
