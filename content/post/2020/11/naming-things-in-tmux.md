---
created: '2024-08-25 15:53:03'
date: 2020-11-21 00:00:00-08:00
description: ''
fname: pub.post.2020.11.naming-things-in-tmux
id: bhraelb3rpbrc8q9smtrna8
redirects:
- /post/2020/11/naming-things-in-tmux/
syndication:
  mastodon: https://hackers.town/@randomgeek/105251184292723132
tags:
- shell
- tmux
- tools
title: Naming Things in tmux
updated: '2024-08-25 15:54:12'
---

In which I sort out which tmux session is which

<!--more-->

I got the basics of [tmux](https://github.com/tmux/tmux) down:

- starting a new session
- creating new windows
- moving between windows
- scrolling back in a window buffer

And that’s about it.

After this long you might expect me to know more.  Alas, no.

At some point I realized you can have more than one tmux session going at a time.  Now my normal day includes the site in one session, work in another, and sometimes a third for random puttering.

I need to manage everything better.

## Using Tmux commands

Although tmux binds keys to commands, it’s easier for me to remember words than keys.  It’s part of why I still use [Taskwarrior]({{< relref "/card/taskwarrior.md" >}}) more than [Org]({{< relref "/card/org.md" >}}).  Because of that, I’ll focus on the tmux commands.

You can send them directly to `tmux` in an open shell.

``` text
tmux <command> [arguments]
```

You don’t have a shell handy?  `C-b :` will pull up a quick Tmux  command prompt to enter your commands:

``` text
C-b :<command> [arguments]
```

If your command produces output, it will display in place of your current window until you hit `ENTER`.

On to the commands themselves.  I’ve added some highlights along the way, with command full names, aliases, and useful arguments — but not *all* arguments.