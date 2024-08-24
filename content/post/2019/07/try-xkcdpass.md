---
created: '2024-04-02 21:25:16'
date: 2019-07-30
description: In which I suggest a password generator
fname: pub.post.2019.07.try-xkcdpass
id: c29juemeazzfkbugpt5v7rs
redirects:
- /2019/07/30/try-xkcdpass/
syndication:
  mastodon: https://hackers.town/@randomgeek/102531070232066570
tags:
- linux
- security
- tools
title: Try Xkcdpass
updated: '2024-04-02 21:27:27'
---

![assets/img/2019/cover-2019-07-30.png](assets/img/2019/cover-2019-07-30.png "[XKCD 936](https://xkcd.com/936/) _([CC BY-NC 2.5](https://xkcd.com/license.html))_")

> [!Summary]
> Use [xkcdpass](https://pypi.org/project/xkcdpass/) to generate more secure passwords, like “correcthorsebatterystaple”.

This started as a Note but I passed my 15 minute rule — if I spend more than 15 minutes on it, it should be a post — so here we are.

It won’t satisfy your bank’s silly password requirements, but — as XKCD told us — using a random collection of words for your password provides more security than trying to [Leet-speak](https://simple.wikipedia.org/wiki/Leet) some word with numbers and symbols.

You could pick a handful of words by flipping through the dictionary, but why not let the computer do it for you? That’s where xkcdpass comes in.

It’s probably available in your package repository.

``` bash
pacman -Ss xkcdpass
```

It’s just Python, so you can use `pip` if you’re on macOS or Windows or some other platform that doesn’t have `xkcdpass` handy.

``` bash
pip install xkcdpass
```

Regardless of how you install it, run it and grab the output — but let your password manager remember it for you.

``` console
$ xkcdpass
tiara embezzle stack doorway scrambled imitate
```