---
aliases:
- /note/2022/01/slowly-pulling-in-tools-for-site-flow/
created: '2024-02-11 13:23:29'
date: 2022-01-16 00:00:00+00:00
description: ''
fname: pub.post.2022.01.slowly-pulling-in-tools-for-site-flow
id: zt7y1crjh5l0fuzbagkhezb
slug: slowly-pulling-in-tools-for-site-flow
syndication:
  mastodon: https://hackers.town/@randomgeek/107634186872393474
tags:
- node-js
- indieweb
- posse
- site
title: Slowly Pulling in Tools for Site Flow
updated: '2024-08-07 19:08:39'
---

Made a [toot](https://hackers.town/@randomgeek/107630284879354154) with [Masto](https://www.npmjs.com/package/masto). Kinda need that for content syndication.

!["I made this toot with Masto in node.js. That sounds weird."](assets/img/2022/toot.png "Here's my toot")

The [Mastodon Twitter Crossposter](https://crossposter.masto.donte.com.br/) works great, but waiting for the announcement toot to show up as a tweet was a tedious manual step that I hope to discard. So I figured out how to make a tweet with [twitter-api-v2](https://www.npmjs.com/package/twitter-api-v2).

Those are the pieces I need to get [POSSE](https://indieweb.org/POSSE) syndication working in this [Eleventy]({{< relref "/card/eleventy.md" >}}) iteration of the site.

Now I just need to staple those pieces together, grab a sharpie, and label it "workflow."