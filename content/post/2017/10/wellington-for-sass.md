---
created: '2024-02-25 05:54:31'
date: 2017-10-31 00:00:00+00:00
description: ''
fname: pub.post.2017.10.wellington-for-sass
id: y8p7sfyh4agmg303exzgp9m
redirects:
- /2017/10/31/wellington-for-sass/
slug: wellington-for-sass
tags:
- site
- css
- tools
title: Wellington for Sass
updated: '2024-08-07 18:48:58'
---

I found [Wellington](https://getwt.io/), a [Sass](http://sass-lang.com/) compiler written in [Go]({{< relref "/card/go.md" >}}).

I installed Wellington with [Homebrew](https://brew.sh/) - actually Linuxbrew but that’s a post for another day maybe, once I’m sure this Linuxbrew experiment worked for me.

```bash
brew install wellington
```

This is not the night to redesign the whole site, though. Make sure everything works.

```console
$ wt compile assets/scss/main.scss -b static/css
2017/10/31 21:09:54 Compilation took: 28.333622ms
```

Seems to produce the same style output. I had no complaint about the speed of Ruby’s Sass compiler, but Wellington is certainly quicker.

I guess now I can start thinking about redesigning the site layout.