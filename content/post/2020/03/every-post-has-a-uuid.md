---
created: '2024-02-13 16:35:59'
date: 2020-03-21 00:00:00+00:00
description: ''
fname: pub.post.2020.03.every-post-has-a-uuid
id: gayyzjb6tbo152nv8qlb851
redirects:
- /note/2020/81/every-post-has-a-uuid/
- /note/2020/03/every-post-has-a-uuid/
slug: every-post-has-a-uuid
syndication:
  mastodon: https://hackers.town/@randomgeek/103864261442692092
tags:
- site
- helpful-hint
title: Every Post Has a Uuid
updated: '2024-02-13 16:36:43'
---

Gave them all a Universally Unique Identifer, per [RFC 4122](http://www.faqs.org/rfcs/rfc4122.html).

Should simplify rearranging the site sources. Helpful hint: don’t rely on filenames as unique content identifiers for your workflow. Oh sure they work fine 80% of the time, but that last 20% is a doozy.

I used Python’s [uuid](https://docs.python.org/3/library/uuid.html) library. There’s also the [uuidgen](http://bigdatums.net/2016/10/01/generate-uuid-linux/) command if I switch away from a Python workflow.

> [!NOTE] 2024-01-14
> Yeah that didn't last. Persistent file paths are way easier to read.