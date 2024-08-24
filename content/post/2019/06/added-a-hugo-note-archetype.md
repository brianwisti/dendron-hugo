---
created: '2024-03-27 16:57:46'
date: 2019-06-23
description: ''
fname: pub.post.2019.06.added-a-hugo-note-archetype
id: ipjrs5mo935e5aratnwdilk
redirects:
- /note/2019/0003/
- /note/2019/174/added-a-hugo-note-archetype/
- /note/2019/06/added-a-hugo-note-archetype/
slug: added-a-hugo-note-archetype
syndication:
  mastodon: https://hackers.town/@randomgeek/102324468805367109
tags:
- notes
- hugo
- posted-from-my-phone
- sort-of
- mobile-hotspot
- my-data-usage-is-gonna-hurt
title: Added a Hugo Note Archetype
updated: '2024-03-27 17:02:55'
---

Moved into a new apartment. Waiting for Internet on Tuesday. It's Sunday.

Continuing to work slow but sure on my notes experiment. Today: a [Hugo]({{< relref "/card/hugo.md" >}}) [archetype](https://gohugo.io/content-management/archetypes/) that includes a full *inbox.iso-8601* timestamp, via [`dateFormat`](https://gohugo.io/functions/dateformat).

```text
---
date: "{{ dateFormat "2006-01-02T15:04:05-07:00" .Date }}"
hashtags:
-
---

SAY SOMETHING
```

And yeah, hashtags are related to but distinct from tags. Basically, I have a particular protocol for tags and posts. I can be more informal with notes and hashtags. The silly name reminds me they're supposed to be fun.

Working out the occasional overlap is a pending item in Taskwarrior.