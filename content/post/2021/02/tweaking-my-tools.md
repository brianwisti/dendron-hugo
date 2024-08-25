---
aliases:
- /note/2021/02/tweaking-my-tools/
created: '2024-02-12 00:12:37'
date: 2021-02-16 00:00:00+00:00
description: ''
fname: pub.post.2021.02.tweaking-my-tools
id: 78r85rt2amigvnfpc5c9kl5
slug: tweaking-my-tools
syndication:
  dev-to: https://dev.to/brianwisti/note-tweaking-my-tools-3f6f
  mastodon: https://hackers.town/@randomgeek/105743422712512318
tags:
- ruby
- site
title: Tweaking My Tools
updated: '2024-08-07 19:04:02'
---

Playing a little more with [TTY Toolkit]({{< relref "/card/ruby/tty-toolkit.md" >}}) for the site workflow. I wanted to say I'm tightening focus, but with a `require` list like this for one tool?

```ruby
require 'pastel'
require 'ruby-slugify'
require 'tty-editor'
require 'tty-exit'
require 'tty-logger'
require 'tty-option'
require 'tty-prompt'
require 'tty-screen'
```

"Tightening focus" would be a lie.

Anyways, it seems to function correctly. Huzzah! Now back to work.