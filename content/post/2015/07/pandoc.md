---
created: '2024-02-23 13:22:07'
date: 2015-07-23
description: ''
fname: pub.post.2015.07.pandoc
id: iydysugumtmzjhisu85djp0
title: Pandoc
updated: '2024-08-07 18:43:47'
---

I could use [Pandoc](http://pandoc.org/) to build HTML from my site
sources.

I could use it to convert them to different sources.

I’m not saying I *would*. But I *could*.

Okay I might.

```bash
pandoc --to org _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.org
pandoc --to asciidoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.adoc
pandoc _posts/programming/2014-12-13-duplicate-files.markdown -o 2014-12-13-duplicate-files.html
```

![Pandoc output in Emacs](assets/img/2015/emacs-pandoc.png)

Honestly at this point I’d say it’s pretty likely.