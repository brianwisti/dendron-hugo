---
aliases:
- /note/2021/10/winget-is-pretty-slick-now/
created: '2024-02-12 04:38:16'
date: 2021-10-16 00:00:00+00:00
description: ''
fname: pub.post.2021.10.winget-is-really-slick-now
id: qrnzgybfsgqj63vysrsv4xz
slug: winget-is-pretty-slick-now
syndication:
  mastodon: https://hackers.town/@randomgeek/107112953002673686
tags:
- windows
- package-manager
- respect-the-command-line
title: Winget Is Really Slick Now
updated: '2024-08-07 19:07:39'
---

Just updated PowerShell via [Winget]({{< relref "/card/winget.md" >}}), Microsoft's command line package manager. And Firefox. And Volta. And HeidiSQL. And Alacritty. And Go. And some other stuff.

Trying to recover a post about [markdown-it-py](https://markdown-it-py.readthedocs.io/en/latest/index.html) that I accidentally deleted, so I won't sidetrack myself with a detailed follow-up to [Winget Preview]({{< relref "/post/2020/06/winget-preview.md" >}}).

Instead, here's the [TIL]({{< relref "/card/til.md" >}}):

`winget upgrade`
: shows what's out of date

`winget upgrade --id=<package.id>`
: upgrades a package

`winget upgrade --all`
: upgrades everything.

No "Run As Administrator" needed, though you need to click the <abbr title="User Access Control">UAC</abbr> dialog. Another caveat: it's coming from the application's own download servers, not some Azure-backed central repository. Sometimes the fetching may take a minute.