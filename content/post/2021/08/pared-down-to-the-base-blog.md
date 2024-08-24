---
created: '2024-02-12 03:59:28'
date: 2021-08-21 00:00:00+00:00
description: ''
fname: pub.post.2021.08.pared-down-to-the-base-blog
id: 60inmluab028owrwshjhs9u
redirects:
- /note/2021/08/pared-down-to-the-base-blog/
slug: pared-down-to-the-base-blog
syndication:
  mastodon: https://hackers.town/@randomgeek/106798500227834335
tags:
- ssg
- site
title: Pared down to the Base Blog
updated: '2024-08-07 19:05:41'
---

![table showing 598 markdown files and 29 reStructuredText files](assets/img/2021/cover-2021-08-21.png "My `rst.txt` files become HTML before the SSG sees, so I may leave them")

No more content shortcodes. No more — or at least not many — exotic content formats. Embedded video or tweet? Copy and paste the embed code from the host site. Need some fancy HTML for notes? Use raw HTML.

I need a base blog, with minimal dependencies on [Hugo]({{< relref "/card/hugo.md" >}}) or any other [Static Site Generator]({{< relref "/card/static-site-generator.md" >}}), so I can get serious with some of those others. "I'd need to port all my shortcodes" has blocked me from switching for the last year and a half (you accumulate a lot of cruft using the same site builder for six years). Now it won't be such a blocker.

Plus, I can try the fancy stuff in [Astro]({{< relref "/card/astro.md" >}}) or [Lektor]({{< relref "/card/lektor.md" >}}) or whatever and still have the base blog to fall back on. Heck, I could port the base blog to [Eleventy]({{< relref "/card/eleventy.md" >}}) or [Zola]({{< relref "/card/zola.md" >}}) or …