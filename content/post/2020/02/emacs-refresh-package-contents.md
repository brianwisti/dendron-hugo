---
aliases:
- /note/2020/59/emacs-refresh-package-contents/
- /note/2020/02/emacs-refresh-package-contents/
created: '2024-02-12 15:42:31'
date: 2020-02-28 00:00:00+00:00
description: ''
fname: pub.post.2020.02.emacs-refresh-package-contents
id: h7dsalxr9x3yv8dcfqptq8a
slug: emacs-refresh-package-contents
syndication:
  mastodon: https://hackers.town/@randomgeek/103737312348546113
tags:
- emacs
- packages
title: Emacs Refresh Package Contents
updated: '2024-08-07 18:59:17'
---

Tried adding [Evil](https://www.emacswiki.org/emacs/Evil)  to [Emacs]({{< relref "/card/emacs.md" >}}) with [Emacs use-package]({{< relref "/post/2019/11/emacs-use-package.md" >}}). Didn’t work.

Didn’t write the error message down, of course. Something about MELPA looking for a package version from two months ago and deciding the package was "Not Found".

Eventually figured out I need to run `package-refresh-contents`, which grabs the latest package listings. Might be overkill to run that automatically in every Emacs session, so I won’t add it to my `.emacs`.

I will add a comment though.

``` elisp
;; Package not installing?
;;  Try 'M-x package-refresh-contents'

(require 'package)
```

Hopefully I remember to read my own comments.

Or the [documentation](https://evil.readthedocs.io/en/latest/overview.html#installation-via-package-el).

> [!NOTE] 2020-04-29
> [john sj anderson](https://genehack.org) wrote a post   [expanding](https://genehack.blog/2020/04/a-bit-of-emacs-advice/) on a [suggestion](https://mastodon.social/@genehack/103737652356761968) to use [advising functions](https://www.gnu.org/software/emacs/manual/html_node/elisp/Advising-Functions.html).
>