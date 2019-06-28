
<!--#echo json="package.json" key="name" underline="=" -->
pywebkitapp-pmb
===============
<!--/#echo -->

<!--#echo json="package.json" key="description" -->
Simple site-specific browser made from Python, GTK and Webkit. App-ify any
URL.
<!--/#echo -->


Features
--------

Icons:
&nbsp; &nbsp; ![☑][ck-hz] = implemented
&nbsp; &nbsp; ![◪][ck-pt] = partially
&nbsp; &nbsp; ![⟎][ck-up] = planned
&nbsp; &nbsp; ![☐][ck-no] = not (yet)

* ![☑][ck-hz] Web browsing within one "tab", just like back in the days
  when usual browsers didn't have tabs.
* ![⟎][ck-up] Support actions that would require to open a new tab/window.
  (For now, at least with links, you can copy their URL and open them in
  a full-fledged browser.)
* Config methods:
  * ![☑][ck-hz] Configure options via env vars `wka_…`. all optional.
  * ![⟎][ck-up] Config via CLI args
* Config options:
  * ![☑][ck-hz] `useragent`: Custom browser name.
  * ![☑][ck-hz] `url`: Which website to display.
  * ![⟎][ck-up] `reloadsec`: Reload the page every … seconds.
  * ![☑][ck-hz] `title`: Window title pattern.
    First character is your dtp (document title placeholder),
    remainder is your window title. All occurrences of the dtp
    (if any) will be replaced with the document title.
  * ![☑][ck-hz] `icon`: Path to an image.
    Image format support might be OS dependent.
    On my Ubuntu, PNG and SVG do work.
  * ![☑][ck-hz] `cwd`: Path to chdir to after initialization (reading
    the `icon` etc.) is complete, before trying to load the `url`.
  * `geometry`:
    `[[width]x[height]][±left±top[±addLeft±addTop]`
    * If it doesn't seem to work, it's probably your window manager trying
      to help you mitigate seemingly ill-advised window placement.
    * ![☑][ck-hz] width, height
    * ![☑][ck-hz] left, top; `±` must be either `+` or `-`,
      negative = Set distance on opposite side.
    * non-standard geometry syntax additions:
      * ![☑][ck-hz] `addLeft` and `addTop` are added to the would-be
        position without any magic, just plain school math.
        Allows to (request to) place (parts of) the window off-screen.
  * ![⟎][ck-up] `winsizelimits`: `minWidth,minHeight,maxWidth,maxHeight`
  * ![☑][ck-hz] `winname`, `wincls`: Window name/class.
  * ![⟎][ck-up] `tweakspy`: Python file to inject for custom config tweaks.



<!--#toc stop="scan" -->


Installation
------------

1. Clone this repo.
1. Install deps as described in the next section.
1. (Optional) Symlink `bin/pywebkitapp-pmb` into `/usr/bin`.



Dependencies
------------

```bash
sudo apt-get --no-install-recommends install \
  python3 python3-gi libgtk-3-0 libwebkitgtk-3.0-0
```



Known issues
------------

* Needs more/better tests and docs.
* `Warning: g_object_…: assertion 'object->ref_count > 0' failed`
  as [explained here][gtk-assertion-failed] seems to be a GTK problem
  unrelated to this project's code, and if you're lucky, might be
  fixable by updating your GTK.





&nbsp;

[gtk-assertion-failed]: http://web.archive.org/web/20190321033524/https://stackoverflow.com/questions/36192975/object-ref-count-0-assertion-failures-when-using-webkitgtk
<!--#sync-icons -->
  [ck-hz]: https://raw.githubusercontent.com/mk-pmb/misc/master/gfm-util/img/checkmark-has.gif# "☑"
  [ck-up]: https://raw.githubusercontent.com/mk-pmb/misc/master/gfm-util/img/checkmark-up.gif# "⟎"
  [ck-pt]: https://raw.githubusercontent.com/mk-pmb/misc/master/gfm-util/img/checkmark-partial.gif# "◪"
  [ck-no]: https://raw.githubusercontent.com/mk-pmb/misc/master/gfm-util/img/checkmark-minus.gif# "☐"
<!--/#sync-icons -->


License
-------
<!--#echo json="package.json" key=".license" -->
ISC
<!--/#echo -->
