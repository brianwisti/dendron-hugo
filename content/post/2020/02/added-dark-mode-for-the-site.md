---
aliases:
- /note/2020/33/added-dark-mode-for-the-site/
- /note/2020/02/added-dark-mode-for-the-site/
created: '2024-02-12 15:41:00'
date: 2020-02-02 00:00:00+00:00
description: ''
fname: pub.post.2020.02.added-dark-mode-for-the-site
id: btr7cdqvemm3jo0my3lqbkl
slug: added-dark-mode-for-the-site
syndication:
  mastodon: https://hackers.town/@randomgeek/103592944673211153
tags:
- site
- css
title: Added Dark Mode for the Site
updated: '2024-02-12 15:42:16'
---

Got tired of blowing my eyeballs out during evening work.

![light web page with dark theme overlaid](assets/img/2020/cover-2020-02-02.png)

How? I used [prefers-color-scheme](https://developer.mozilla.org/en-US/search?q=prefers-color-scheme). It tries to respect existing light/dark mode settings. Here’s the stylesheet short version.

``` scss
:root {
  --text-color:                 hsl(0, 0%, 0%);
  --content-background-color:   hsla(0, 0%, 100%, 0.8);
}

@media (prefers-color-scheme: dark) {
  :root {
    --text-color:               hsl(0, 0%, 100%);
    --content-background-color: hsla(0, 0%, 0%, 0.8);
  }
}

#page-content {
   background-color: var(--content-background-color)
   color:            var(--text-color);
}
```