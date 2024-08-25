---
aliases:
- /2020/02/04/goto-address-mode-opens-links-in-emacs/"
created: '2024-02-13 14:34:28'
date: 2020-02-04 00:00:00+00:00
description: Use `goto-address-mode` to make links in Emacs buffers clickable
fname: pub.post.2020.02.goto-address-mode-opens-links-in-emacs
id: ia2xwbr7emmbaxu5unaq9d9
slug: goto-address-mode-opens-links-in-emacs
tags:
- emacs
- tools
title: Goto Address Mode Opens Links in Emacs
updated: '2024-08-07 18:59:22'
---

![Emacs view of reStructuredTExt with a link highlighted as clickable](assets/img/2020/cover-2020-02-04.png)

[Org]({{< relref "/card/org.md" >}}) mode has this nice thing where you can click a link in the [Emacs]({{< relref "/card/emacs.md" >}}) buffer to open it in your browser. Turns out that’s not some special org-only behavior. It’s [goto-address-mode](https://www.gnu.org/software/emacs/manual/html_node/emacs/Goto-Address-mode.html), a minor mode that activates URLs and email addresses in the current buffer.

You can manually launch it with `M-x goto-address-mode`. It might be easier to automatically enable it for certain modes. You do that with a [hook](https://www.gnu.org/software/emacs/manual/html_node/emacs/Hooks.html).

I want links to be available when reviewing notes and blog posts. Since I write those notes in a number of formats, I should add the hook one of the general [major modes](https://www.gnu.org/software/emacs/manual/html_node/elisp/Basic-Major-Modes.html#Basic-Major-Modes). text-mode is a good start.

``` lisp
;; base mode for prose
(add-hook 'text-mode-hook (lambda ()
                           (goto-address-mode)))
```

Now I can open links from my Markdown and [reStructuredText]({{< relref "/card/restructuredtext.md" >}}) files with a click! Or a `C-c <RET>`.

**`goto-address-mode` key bindings**

| Key         | Function                | Action                     |
| ----------- | ----------------------- | -------------------------- |
| `C-c <RET>` | `goto-address-at-point` | Opens the link under point |

I might add the hook for prog-mode later, if I find myself wanting to click URLs in source code.