---
aliases:
- /blogspot/2007/02/03_late-night-thoughts-about-fm.html
- /post/2007/late-night-thoughts-about-fm/
created: '2024-02-18 04:23:00'
date: 2007-02-03 00:00:00+00:00
description: ''
fname: pub.post.2007.02.late-night-thoughts-about-fm
id: lsxdb1041sj8jvcw4c4kbmb
slug: late-night-thoughts-about-fm
tags:
- blogspot
- now
title: Late Night Thoughts about Fm
updated: '2024-08-07 18:31:27'
---

FM. FXRuby Media. Or f-m, as known on Rubyforge. I probably should have gone for fmm or something like that, but these things are always more obvious when it is too late.

Oh right. I had thoughts.

Development of version 1 is moving along swimmingly. The basic Track abstraction is in place, along with the code to create Track objects when given MP3 and M4A files. That's all for now, because that's what I have. More formats will be supported as I need them or as users submit the needed TrackFormat code.

And I've almost made it to the heel on my knitted sock. The last couple of days have just been loaded with accomplishments.

I noticed that [ruby-mp3info](https://github.com/moumar/ruby-mp3info) and [mp4info](https://github.com/arbarlow/ruby-mp4info) were choking on a couple of the files in my library. There needs to be a solid way to test both of them against a reasonably large dataset so I can find the issue and fix it. Oh, I know! I can use my iTunes Library XML file as a reference ...

1. parse the XML file, creating a hash of hashes — track information keyed to filenames
2. Send ruby-mp3info and mp4info chugging along in my Music library, comparing parsed results to those claimed by the XML file

It'll take a while, but at least I will know if my fixes break something else. That's always handy for patches.

Version zero of FM used [SQLite]({{< relref "/card/sqlite.md" >}}) for storing track details. I might do that again, but I am also taking a serious look at [KirbyBase](https://github.com/gurugeek/KirbyBase/). I really like the idea of using [Ruby]({{< relref "/card/ruby/_index.md" >}}) code for my query. Installed system libraries matter less when your application relies less on non-Ruby code. Then again, I had a nice little abstraction layer on top of the SQL calls which already makes my life easy enough for this app.  It wasn't as pretty as real code, though.  Maybe I'll try both.  Maybe I'll just use KirbyBase.  Maybe I'll stick to the practical side of lazy for now and keep using SQLite. This is my project, so it's subject to my whims.

FM files won't be available for at least a week. I want to have something that approximates what I have now (plus tests) before I go posting code all over the globe.

I also need to do a little research on mock objects (for testing the database layer) and — what do they call it when you automate UI testing?  Well, whatever they call it. That's something else I want to look into.

It's 3:21. I'm coding, blogging, drinking wine, and watching Black Books. Fun as all that is, I think it's time for sleep.