---
created: '2024-08-25 14:19:49'
date: '2020-05-09T03:25:00.000Z'
description: ''
fname: pub.post.2020.05.debugging-my-site-with-a-little-help-from-my-friends
id: 7yy573gn3ff5s32llefzx1b
redirects:
- /note/2020/05/debugging-my-site-with-a-little-help-from-my-friends/
syndication:
  mastodon: https://hackers.town/@randomgeek/104136380782825124
tags:
- indieweb
- data
- i-fixed-it
- before-i-pushed-it
- yay-for-tests
title: Debugging My Site with a Little Help from My Friends
updated: '2024-08-25 14:23:00'
---

![cover-2020-05-08.png](assets/img/2020/cover-2020-05-08.png))

> It’s probably redundant to test HTML structure for my pages, but [what the heck]({{< relref "/post/2020/03/passing-tests-is-now-required-to-push.md" >}})
>
> -- <cite>Me, a couple months ago</cite>

> There’s no rule, but *obviously* every webmention to my site will have
> full author info including photo.
>
> -- <cite>Me, a few weeks ago</cite>

> Look honey I added [Webmention]({{< relref "/card/webmention.md" >}}) data to my [Datasette dashboard]({{< relref "/post/2020/05/datasette-sure-is-nifty.md" >}})!
>
> -- <cite>Me, this morning</cite>

> Sweet, jmac liked my [mention]({{< relref "/post/2020/05/pondering-my-indieweb-guinea-pig.md" >}})!  Wait why are tests failing? Maybe check
> the dashboard?
>
> -- <cite>Me, an hour ago</cite>

> I fixed it!
>
> -- <cite>Me, a few minutes ago</cite>

The fix is reasonable defaults for response author info. I got other fixes in mind, including a default "card" for anonymous response authors. Also, inferring author info from source site. Thanks for the help and the ideas, [Jason McIntosh](https://jmac.org)!