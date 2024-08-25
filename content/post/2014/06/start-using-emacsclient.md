---
aliases:
- /emacs/2014/06/02_start-using-emacsclient.html
- /post/2014/start-using-emacsclient/
created: '2024-02-22 17:34:57'
date: 2014-06-02 00:00:00+00:00
description: ''
fname: pub.post.2014.06.start-using-emacsclient
id: j9rnhqbie5mb5wrztbq81i5
slug: start-using-emacsclient
tags:
- emacs
- tools
title: Start Using Emacsclient
updated: '2024-08-07 18:40:37'
---

I have been curious about the [Emacs Client](http://www.emacswiki.org/emacs/EmacsClient) for a long time. Because [Emacs]({{< relref "/card/emacs.md" >}}) can have a long startup time, it can be made to run in a persistent mode. All buffers are handled by a central process. Your editor interface connects to that central process rather than managing its own buffers. Thinking about the Emacs client is what started me down the path of studying Emacs as a client/server Lisp environment. Anyways, I looked up some blog posts to tell me what to do.
<!--more-->

It should not surprise me that a [blog post](http://devblog.avdi.org/2011/10/27/running-emacs-as-a-server-emacs-reboot-15/) by Avdi Grimm is one of the top hits for Emacs Client - or anything else, really. I am willing to bet that all of his [Emacs Reboot](http://devblog.avdi.org/category/emacs-reboot/) posts are worth reading and reviewing. Let's focus on just the one post for now.

He mentions having a short script `ec` to simplify invocation of `emacsclient`.

``` sh
#!/bin/sh
exec /usr/bin/env emacsclient -c -a "" $*
```

I was tempted to create an alias, but his solution will work regardless of which shell I happen to be fiddling around with that day.

I'm also inclined to follow his thought of removing the keybinding for `save-buffers-kill-terminal` and `suspend-frame`. There have already been a few times where I quit when I meant to save.

``` emacs-lisp
;; Adding this to my ~/.emacs.d/init.el
(global-unset-key (kbd "C-x C-c"))
(global-unset-key (kbd "C-x C-z"))
```

I use [elscreen](http://www.emacswiki.org/emacs/EmacsLispScreen). Since `emacsclient` keeps everything running, you can switch back to a previously active screen with `C-z b`. So that makes these the new important commands for me to remember.

| Function                          | Keybinding       | Description                         |
|-----------------------------------|------------------|-------------------------------------|
| `delete-frame`                    | `C-x 5 0`        | "Quit" an emacsclient session       |
| `elscreen-find-and-goto-by-buffer`| `C-z b <buffer>` | Switch to screen holding `<buffer>` |
| `kill-emacs`                      | *None*           | Shut down Emacs                     |

It would probably be a good idea to set up a `kill-emacs-hook` or make a custom shutdown function. EmacsWiki offers [this suggestion](http://www.emacswiki.org/emacs/EmacsAsDaemon#toc7).

Can't help noticing that the `delete-command` command learned in a GUI context applies for `emacsclient` as well. Curious. There are bound to be new issues. Expect a "my bad" post in the future when I find out what those new issues are.