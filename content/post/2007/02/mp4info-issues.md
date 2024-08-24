---
created: '2024-02-18 04:24:07'
date: 2007-02-12 00:00:00+00:00
description: ''
fname: pub.post.2007.02.mp4info-issues
id: 8xsgsqvcu6wc804kx6c6dmj
redirects:
- /blogspot/2007/02/12_mp4info-issues.html
- /post/2007/mp4info-issues/
- /2007/02/12/mp4info-issues/
slug: mp4info-issues
tags:
- ruby
- blogspot
title: Mp4info Issues
updated: '2024-08-07 18:31:32'
---

> [!NOTE] 2015-03-28
> No idea whether this is still true, or even if it was just something stupid I was doing in 2007.

[mp4info](https://github.com/arbarlow/ruby-mp4info) thinks that my 5 minute Bob Newhart track is 2 seconds long. Looks like that is an issue on several tracks. I need to dig into that, see why [Perl]({{< relref "/card/perl.md" >}})'s MP4::Info picks up the correct length but the [Ruby]({{< relref "/card/ruby/_index.md" >}}) counterpart does not.