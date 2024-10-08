---
aliases:
- /note/2020/36/inv-note/
- /note/2020/02/inv-note/
banner:
  alt: tiled symmetry drawing in green and yellow tones
  caption: I drew this with Amaziograph
  href: assets/img/2020/cover-2020-02-05.jpg
created: '2024-02-13 14:38:59'
date: '2020-02-05T00:00:00.000Z'
description: ''
fname: pub.post.2020.02.inv-note
id: 2j3v18889se9y4oj8c8351f
slug: inv-note
syndication:
  mastodon: https://hackers.town/@randomgeek/103607162408116784
tags:
- site
- pyinvoke
- drawing
- amaziograph
- fun
title: inv note
updated: '2024-08-25 14:05:51'
---

![tiled symmetry drawing in green and yellow tones](assets/img/2020/cover-2020-02-05.jpg "I drew this with Amaziograph")

```sh
inv note --title='inv note'
```

Don’t mind me. I’m just trying an experiment with using [Pyinvoke]({{< relref "/card/pyinvoke.md" >}}) for my site workflow instead of [Make](https://www.gnu.org/software/make/).

```console
$ inv serve
SHOW_INFO=1 hugo server --buildDrafts --bind 0.0.0.0 --navigateToChanged
...
Press Ctrl+C to stop
```

But that’s boring on its own. Here. Have a drawing.

I’ll probably make a proper blog post about Invoke later. Meanwhile, checkout the docs on [Getting started](https://docs.pyinvoke.org/en/stable/getting-started.html).

```sh
inv publish
```