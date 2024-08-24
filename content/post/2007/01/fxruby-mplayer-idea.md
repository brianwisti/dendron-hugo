---
created: '2024-02-18 04:21:26'
date: 2007-01-30 00:00:00+00:00
description: ''
fname: pub.post.2007.01.fxruby-mplayer-idea
id: sxcrb066i574y65nrjdb3ap
redirects:
- /blogspot/2007/01/30_fxruby-mplayer-idea.html
- /post/2007/fxruby-mplayer-idea/
- /2007/01/30/fxruby-mplayer-idea/
slug: fxruby-mplayer-idea
tags:
- blogspot
title: FXRuby MPlayer Idea
updated: '2024-08-07 18:31:21'
---

![iTunes-like music player application](assets/img/2007/cover-2007-01-30.png)

A few weeks back I wrote up a GUI front-end for [mplayer](https://www.mplayerhq.hu). It works nice enough, but it suffers from a few aesthetic issues.

It's written in [Perl]({{< relref "/card/perl.md" >}}), with [POE](https://metacpan.org/pod/POE) and [Perl/Tk](https://metacpan.org/pod/distribution/Tk/Tk.pod). I managed to write the code in such a way that it's readable, but ... well, Perl/Tk looks like ass. It's okay for smaller projects, but it becomes more and more obvious as your project grows that it's just not pretty enough. Tcl/Tk has [Tile](https://tktable.sourceforge.net/tile), which would make things all pretty, but I'm not comfortable writing apps with Tcl. POE is also okay, but I have no POE-fu to speak of. So the application code is also starting to look like ass.

MPlayer slave mode is not working completely as advertised, or it's not interacting well with my POE-ass code. Whatever. Pause does not actually pause. It just hiccups for a second and goes back to playing. I will work around that, but I'll also be keeping my eyes open for something else.

I have chosen to rewrite the front end with [Ruby]({{< relref "/card/ruby/_index.md" >}}) - specifically [FXRuby](https://github.com/larskanis/fxruby). I might have used [Ruby/Gtk2](https://ruby-gnome.github.io), but for some reason I can't convince this stupid computer that I have the Gtk2 development libs. Score one more point of hate for Redhat-based distros.

Yes, the basic interface is familiar. No, it's not a clone. All this baby is planned to do is import, organize, and play your music files. Even then, you are probably better off with the original if it's available for your platform.