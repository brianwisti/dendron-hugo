---
created: '2024-08-25 14:42:14'
date: 2020-05-07 14:30:00-07:00
description: ''
fname: pub.post.2020.05.made-an-emacs-binding-for-config-quick-edit
id: xjuj0dreavflix6x6522yq9
redirects:
- /note/2020/05/made-an-emacs-binding-for-config-quick-edit/
syndication:
  mastodon: https://hackers.town/@randomgeek/104129350946938060
tags:
- emacs
- orgconfig
title: Made an Emacs Binding for Config Quick Edit
updated: '2024-08-25 14:43:13'
---

I hit `F5`, [Emacs]({{< relref "/card/emacs.md" >}}) opens my `config.org` for editing. It might not be much but it feels good to scratch such a specific itch. Feeling pretty good about myself.

``` lisp
(global-set-key (kbd "<f5>")
                (lambda ()
                  (interactive)
                  (find-file "~/.dotfiles/config.org")))
```