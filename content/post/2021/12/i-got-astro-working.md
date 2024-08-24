---
created: '2024-02-12 04:48:56'
date: 2021-12-23 00:00:00+00:00
description: ''
fname: pub.post.2021.12.i-got-astro-working
id: 0uahrwo8vddqjsooltbwtlk
redirects:
- /note/2021/12/i-got-astro-working/
slug: i-got-astro-working
syndication:
  mastodon: https://hackers.town/@randomgeek/107498629085558103
tags:
- astro-dot-build
- ssg
- site
title: I Got Astro Working
updated: '2024-08-07 19:07:49'
---

![Web page showinging latest note and listing recent posts](assets/img/2021/cover-2021-12-23.png "this time you get a screenshot")

[Astro]({{< relref "/card/astro.md" >}}) is great once you get started. A bit funky if you have twenty years of legacy content.

Rather than do my usual — a screenshot and *maybe* a "lesson learned" post — this time around I made a public [repo](https://github.com/brianwisti/rgb-astro) and [live instance](https://quirky-wozniak-e4e36f.netlify.app) of this in-progress experiment available for your entertainment and edification.

Oh and lesson learned: components are *fussy*, and the errors don't always happen where you expect. Treat all your imported HTML as XHTML, and look for stray `{` characters. You might need to convert those to `&#123;`.

Took me months to figure that out. Hopefully it saves you a few hours of confusion.