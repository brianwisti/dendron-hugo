---
created: '2024-02-22 16:48:50'
date: 2014-05-24 00:00:00+00:00
description: ''
fname: pub.post.2014.05.the-emacs-tutorial-as-elisp-tour
id: wb7vs9zhfvnben93jv0jse5
redirects:
- /emacs/2014/05/24_the-emacs-tutorial-as-elisp-tour.html
- /post/2014/the-emacs-tutorial-as-elisp-tour/
- /2014/05/24/the-emacs-tutorial-as-elisp-tour/
slug: the-emacs-tutorial-as-elisp-tour
tags:
- emacs
- elisp
- tutorial
- tools
title: The Emacs Tutorial as Elisp Tour
updated: '2024-08-07 18:40:20'
---

I am trying to *really* learn how to use [Emacs]({{< relref "/card/emacs.md" >}}). One thing that strikes me is how the Emacs user interface can be thought of as a client application to an Emacs Lisp API. This is not a revolutionary thought, but it really stuck in my head. I reread the official tutorial, focusing on the functions rather than the keybindings that invoke them.
<!--more-->

The first function is obviously the one to get the tutorial started.

 Function             | Keybinding | Description
----------------------|------------|-----------------------------------------
 `help-with-tutorial` | `C-h t`    | Launch the Emacs learn-by-doing tutorial

Then I spent a couple days with liberal usage of `describe-key` and `describe-function` to better understand what the tutorial was describing. It was helpful. Now I just want to organize those notes and post them on the blog.

Or I could dump the list into a blog post: [Elisp Functions Described in the Emacs Tutorial]({{< relref "/post/2014/05/elisp-functions-described-in-the-emacs-tutorial.md" >}})