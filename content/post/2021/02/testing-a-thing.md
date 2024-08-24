---
created: '2024-02-11 23:55:59'
date: 2021-02-14 00:00:00+00:00
description: ''
fname: pub.post.2021.02.testing-a-thing
id: cl9uih8e19xbez4iwthsmj8
redirects:
- /note/2021/02/testing-a-thing/
slug: testing-a-thing
syndication:
  dev-to: https://dev.to/brianwisti/note-testing-a-thing-ad3
  mastodon: https://hackers.town/@randomgeek/105732993013826473
tags:
- asciidoctor
- hugo
- site
title: Testing a Thing
updated: '2024-08-07 19:03:57'
---

[Letting Ruby Build Asciidoctor Files for Hugo]({{< relref "/post/2020/05/letting-ruby-build-asciidoctor-files-for-hugo.md" >}}) was half of a great idea for better [Asciidoctor]({{< relref "/card/asciidoctor.md" >}}) handling in [Hugo]({{< relref "/card/hugo.md" >}}). I *might* have the other half now:

* keep my content in the content folder.
* Use `adoc.txt` for the extension so Hugo ignores it.
* Point my `build-adoc` script there instead of a neighboring `adoc` folder.
* profit?

Would work for [reStructuredText]({{< relref "/card/restructuredtext.md" >}}) too.

Need to get through a few post cycles to see how it works.