---
aliases:
- /2019/11/09/emacs-use-package/
created: '2024-02-12 22:31:26'
date: 2019-11-09 00:00:00+00:00
description: Just declared `.emacs` bankruptcy. Starting over with `use-package`.
fname: pub.post.2019.11.emacs-use-package
id: 3t8w6j8q3es4hub61m19l45
slug: emacs-use-package
tags:
- emacs
- packages
- tools
title: Emacs use-package
updated: '2024-08-25 17:12:44'
---

I admit it. My [Emacs]({{< relref "/card/emacs.md" >}}) usage is intermittent at best. But I do use Emacs *sometimes*. Still haven’t found anything to match [Org]({{< relref "/card/org.md" >}}) for taking notes or writing posts.

So until I find something better than Org mode — which may take a while — I need Emacs. That means I need to get better at using it. *That* starts with configuration that isn’t a tribute to the [Flying Spaghetti Monster](http://spaghettimonster.com).

[use-package](https://github.com/jwiegly/use-package) helps organize loading and configuring Emacs packages. I need it.

## My new `~/.emacs`

I start with a prelude, telling Emacs about package manager details: mainly where to find packages and to install `use-package` if it isn’t already available.

``` lisp
;;
;; package manager setup
;;

(require 'package)

(add-to-list 'package-archives '("org" . "https://orgmode.org/elpa/"))
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))

(setq package-enable-at-startup nil)
(package-initialize)

(unless (package-installed-p 'use-package)
 (package-refresh-contents)
 (package-install 'use-package))

(eval-when-compile
 (require 'use-package))
```

> [!WARNING]
> Trailing slashes are important! `melpa.org/packages/` gets a list. `melpa.org/packages` does not.

Next I tell use-package that I want org.

``` lisp
;;
;; Load and configure packages
;;

;; org of course
(use-package org
 :ensure org-plus-contrib
 :config
 (setq org-agenda-files(quote ("~/Dropbox/org/agendas/tasks.org")))
 (global-set-key "\C-cl" 'org-store-link)
 (global-set-key "\C-cc" 'org-capture)
 (global-set-key "\C-ca" 'org-agenda))
```

The additional options are where the `use-package` approach gets interesting to me. I can insist the package be installed with `:ensure t` — or as in this case, ensure that another package be installed to meet my requirements.

`:config` provides code that gets executed after `org` is loaded. Pretty minimal so far, but the thing is — well, there’s a couple things:

- `:config` code won’t execute if the package doesn’t load; that keeps the  Emacs session tidy.
- All the configuration relevant to `org` is right there in one place.

So later tonight when I add [Elscreen]({{< relref "/post/2017/01/elscreen.md" >}}) and [Emacs Writegood Mode]({{< relref "/post/2017/08/emacs-writegood-mode.md" >}}), I can keep all their configuration details together with minimal effort. It’s the default pattern with `use-package`. That’s promising.

That’s the package management out of the way. The rest is a couple settings I already know I want, to satisfy muscle memory and streamline prose editing.

``` elisp
;;
;; Preferences not covered already by packages or custom
;;

;; Invoke M-x without Alt
(global-set-key "\C-x\C-m" 'execute-extended-command)

;; Wrap long lines when editing text
(add-hook 'text-mode-hook 'turn-on-auto-fill)
```

Finally is `custom-set-variables`, already filling up with automated customizations. My bad habits include hand-editing these values, so I put in a reminder to stop doing that.

``` elisp
;;
;; Custom settings. Try to leave them alone.
;;

(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
  '(package-selected-packages (quote (use-package))))
```

Done! Now let’s see how tidy I can keep my `.emacs` file.

## What next

Not sure, really. Install `elscreen` and `writegood-mode`.  Maybe revisit
Rainer König’s [OrgMode Tutorial](https://www.youtube.com/playlist?list=PLVtKhBrRV%5FZkPnBtt%5FTD1Cs9PJlU0IIdE) videos.  [ox-hugo](https://ox-hugo.scripter.co/) also looks pretty interesting!

Okay that last is a little disengenous. `ox-hugo` looked interesting enough that I used it to write this post. I might talk about that more once I have a better idea what I’m doing.