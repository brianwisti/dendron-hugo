---
created: '2024-02-12 03:57:55'
date: 2021-09-16 00:00:00+00:00
description: ''
fname: pub.post.2021.09.finally-have-all-my-content-in-one-format
id: wvi2myatonio8za65trlg6v
slug: finally-have-all-my-content-in-one-format
syndication:
  mastodon: https://hackers.town/@randomgeek/106945161649678603
tags:
- site
- asciidoctor
title: Finally Have All My Content in One Format
updated: '2024-08-07 19:05:55'
---

```plaintext
content/**/*{.md,.md.txt,.rst,.rst.txt,.adoc,.adoc.txt,.org}
┌─────────┬─────┐
│Format   │Count│
├─────────┼─────┤
│.md      │48   │
│.adoc.txt│574  │
│.md.txt  │579  │
│.rst.txt │32   │
└─────────┴─────┘
```

Okay yes I also have it in several other formats. Came up with an approach where I can keep all my formats in the [Pared down to the Base Blog]({{< relref "/post/2021/08/pared-down-to-the-base-blog.md" >}}) and build whatever I prefer.

My *point* is that all the content that counts is available in [Asciidoctor]({{< relref "/card/asciidoctor.md" >}}) format. Better choice for me than Markdown since Asciidoctor already has built-in understanding of notes and asides. Better choice for me than [reStructuredText]({{< relref "/card/restructuredtext.md" >}}) because it's easier to find Asciidoctor processors for assorted static site generators.