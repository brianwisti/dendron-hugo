---
aliases:
- /post/2020/06/ox-hugo-for-the-orgconfig/
created: '2024-08-25 15:24:31'
date: 2020-06-27 00:00:00-07:00
description: ''
fname: pub.post.2020.06.ox-hugo-for-the-orgconfig
id: usio60yasrk61kk0bd0e9ta
tags:
- orgconfig
- orgmode
- site
- tools
title: ox-hugo for the Orgconfig
updated: '2024-08-25 15:27:50'
---

![cover-2020-06-27](assets/img/2020/cover-2020-06-27.png)

Putting a couple how-to details down for easy searching later

<!--more-->

## What?

I’m combining all my [Org]({{< relref "/card/org.md" >}}) config files into one, and then using [`ox-hugo`](https://ox-hugo.scripter.co) to generate Markdown files for my [Hugo]({{< relref "/card/hugo.md" >}}) site.

## Why?

Hugo renders Org files just fine, but I wanted my config to be a bit more tightly integrated.  `ox-hugo` works well as both plain old Org and as an intermediary that exports Hugo content.  A single Org file can become as many Hugo pages as I want.

## Getting it to work

This week my favorite Emacs flavor is [Doom Emacs](https://github.com/hlissner/doom-emacs).  Their [org module](https://github.com/hlissner/doom-emacs/tree/develop/modules/lang/org) supports `ox-hugo` as an option, so enabling that option in my init should do the trick — after a `doom sync` of course.

``` lisp
(doom!
 ⋮
 :lang
 (org +hugo))
```

Off in the depths of my `~/org/` folder, I create a new `config.org`.

``` org
#+title: My Orgconfig
#+hugo_base_dir: ~/Sites/random-geekery-blog/
#+hugo_section: config
```

Everything here will end up going in the `config` section of my site, under `~/Sites/random-geekery-blog/content/config`.

> [!NOTE]
> A while back I got stuck with `ox-hugo` for my site because of how big each section is.  Using an Org file per section might work really well!  It works great for this case, that’s for sure.

Each top-level section will be a page in `/config/`. I show *which* page in the subtree’s `:properties:`.

``` org
+ Emacs config
:properties:
:export_description: Be kinda weird if I didn't manage that one in Org, yes?
:export_file_name: emacs
:export_hugo_weight: 5
:end:
```

`ox-hugo` automatically [converts](https://ox-hugo.scripter.co/doc/org-meta-data-to-hugo-front-matter/%5D) the `export` properties to Hugo front matter.  `:export_file_name:` of `emacs` maps out to a generated file `emacs/index.md` under `content/config/`.

> [!WARNING]
> If you’re playing along, remember to tag sensitive config sections as `:noexport:`!

Since I’m showing off [Babel](https://orgmode.org/worg/org-contrib/babel/intro.html)’s ability to tangle, I want to show the tangle references.  `:noweb no-export` tells Babel to tangle when evaluating the block, but *not* when exporting.

``` org
#+name: zsh/base-variables
#+begin_src text :noweb no-export
<<zsh/set-base-path>>
<<zsh/define-editor>>
<<zsh/clicolor>>
<<zsh/add-home-bin>>
#+end_src
```

And — yeah.  I still haven’t figured out a nice way to highlight those tangle bits, so for the moment I default to calling my mostly-tangled blocks "text".

I also create a subtree for the section `_index.md`.

``` org
+ My personal orgconfig
:properties:
:export_file_name: _index
:end:

#+begin_note
This is my live config, written as an [[https://orgmode.org/][Org]] file and integrated with my site with [[https://ox-hugo.scripter.co/][=ox-hugo=]].
⋮
```

Now my config section summary is part of the config org file.  I find this aesthetically pleasing.

## The rest is implementation details

This whole process is fiddly.  Org mode.  Literate config.  Hugo.  `ox-hugo`. That makes the whole thing fiddly^4 or something.  But these quick notes covered things that got in my way while gluing the whole thing together.  If you want to try it out, at least *some* of the fiddliness should be clearer.