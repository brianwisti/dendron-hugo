---
created: '2024-02-12 03:11:22'
date: 2021-05-14 00:00:00+00:00
description: ''
fname: pub.post.2021.05.oh-no-i-added-a-javascript-search-thing
id: rvswulu2ry2rcjiyxooj7iv
redirects:
- /note/2021/05/oh-no-i-added-a-javascript-search-thing/
slug: oh-no-i-added-a-javascript-search-thing
syndication:
  mastodon: https://hackers.town/@randomgeek/106236540435473063
tags:
- site
- javascript
- hyperscript
title: Oh No I Added a JavaScript Search Thing
updated: '2024-08-07 19:05:09'
---

And a touch of [\_hyperscript](https://hyperscript.org/).
Started from [this post](https://makewithhugo.com/add-search-to-a-hugo-site/) and leaned on the \_hyperscript to tie some bits together.

```html
<button _="on click
           get value of #searchQuery
           call executeSearch(it, false)">Search</button>

```

And yeah I'm back on [Hugo]({{< relref "/card/hugo.md" >}}). Spent so much time in the last couple weeks touching up the static repo and ignoring the [Statamic]({{< relref "/card/statamic.md" >}}) live site. Decided not to fight it. Anyways, now that I started clearly the logical next step will be [Gatsby]({{< relref "/card/gatsby.md" >}}). For flexible values of "logical."