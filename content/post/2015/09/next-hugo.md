---
aliases:
- /post/2015/hugo/
- /2015/09/27/next-hugo/
created: '2024-02-11 13:29:22'
date: 2015-09-27 20:36:30+00:00
description: I Rebuilt Random Geekery with Hugo
fname: pub.post.2015.09.next-hugo
id: k9xj90zw3l53liml8l07k06
slug: next-hugo
tags:
- site
- hugo
- tools
title: Next? Hugo
updated: '2024-08-07 18:44:38'
---

Hey it has been a while since I shuffled the site around completely. I'll
just redo the whole thing in [Hugo]({{< relref "/card/hugo.md" >}}).

<!--more-->

[Jekyll]({{< relref "/card/jekyll.md" >}}) is nice enough, but the long build times are tiresome. Even the 3.0 beta drags once your site gets complex. A fresh build usually took 15 seconds, and some unoptimized template experimentation pushed that up briefly to 45 seconds.

I spent a few days converting this site to Hugo. So far the longest the site has taken to build is 350 milliseconds. Plus it automatically handled the [reStructuredText]({{< relref "/card/restructuredtext.md" >}}) posts. I think it hands them off to `rst2html` but I have not checked that yet. No plugin is needed. That is nice.

All the URLS have been changed, but hopefully you won't notice thanks to [aliases](http://gohugo.io/extras/aliases/). Plus I got the basics of [taxonomies](http://gohugo.io/taxonomies/overview/) well enough to get categories and tags working. One way or another you should still be able to find content that people were actually viewing. Things like the Crafts collection will wait until I get a better understanding of taxonomy in Hugo.

The site looks nice because of the [Hyde-X](https://github.com/zyro/hyde-x) theme. Of course I already modified the theme for my own visual and organizational aesthetics. It'll probably look completely different by the time I'm done. Hyde-X gives a great starting point though.

> [!NOTE] 2024-01-13
> And now my theme is derived from [Poison](https://themes.gohugo.io/themes/poison/), another Hyde-inspired theme. I have come full circle!

Okay I need to get back to it. There are a lot of rough edges to smooth out.