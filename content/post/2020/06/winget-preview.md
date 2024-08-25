---
created: '2024-02-12 04:40:04'
date: '2020-06-14T00:00:00.000Z'
description: ''
fname: pub.post.2020.06.winget-preview
id: um9mnjf4sn6v7m861fbn1nc
slug: winget
syndication:
  mastodon: https://hackers.town/@randomgeek/104344729509760889
tags:
- windows
- package-manager
- tools
title: Winget Preview
updated: '2024-08-25 15:32:00'
---

Trying out another windows package manager

<!--more-->

[Winget]({{< relref "/card/winget.md" >}}) is a command line package manager for [Windows]({{< relref "/card/windows.md" >}}) 10, open-sourced under the [MIT License](https://github.com/microsoft/winget-cli/blob/master/LICENSE).  Roughly equivalent to `apt` or `brew`.  If you already know and love [Chocolatey](https://chocolatey.org/), you’re fine.  Stick with that for now. `winget` shows promise though.

The other night I installed [Strawberry Perl](https://strawberryperl.com) and played with [Image::ExifTool](https://metacpan.org/release/Image-ExifTool) a tiny bit.

Yesterday I successfully installed Emacs and started doing real work writing Perl code with it.

Exciting!

Well, not *work* work. The new job doesn’t start until tomorrow, and is mostly Python.

## How do I get Winget?

`winget` is still in preview.  You can get it as part of the [Windows Insider](https://insider.windows.com/) program, like me.  Slow Ring should be fine.  If you don’t feel like taking the risk on a preview release of Windows, you can grab it from the [winget-cli repository](https://github.com/microsoft/winget-cli).

## Finding and installing stuff with ``winget``

One goal when in Windows is to *use* Windows, and not just spend all day hiding
in WSL.  If I want to use Windows, I need [Perl]({{< relref "/card/perl.md" >}}).

Hey, I’ll allow myself a few crutches here and there.

``` text
PS > winget search perl
Name            Id                            Version  Matched
----------------------------------------------------------------
Strawberry Perl StrawberryPerl.StrawberryPerl 5.30.2.1
Xampp           ApacheFriends.Xampp           7.4.6    Tag: Perl
```

Ooh, [XAMPP](https://www.apachefriends.org/index.html).  I haven't messed with that in years.

But no I'm just here for Perl today.  Strawberry Perl is an excellent Perl setup for Windows.  Provides all the core stuff, a bunch of [useful extras](http://strawberryperl.com/release-notes/5.30.2.1-64bit.html), and the tools you need to install additional libraries.

`winget show` displays additional details about a package.

``` text
PS > winget show StrawberryPerl
Found Strawberry Perl [StrawberryPerl.StrawberryPerl]
Version: 5.30.2.1
Publisher: strawberryperl.com project
Description: Strawberry Perl is a perl environment for MS Windows containing all you need to run and develop perl
applications. It is designed to be as close as possible to perl environment on UNIX systems.
Homepage: http://strawberryperl.com/
License: Perl.org
Installer:
  SHA256: 2365e89623b496ca530443a362e765f3e8de9daa744b07924b17ae7aa0b06002
  Download Url: http://strawberryperl.com/download/5.30.2.1/strawberry-perl-5.30.2.1-32bit.msi
  Type: Msi
```

Yep, that's what I want.

``` text
PS > winget install StrawberryPerl
```

Things do get automatically added to your path, but not right away.  Somebody more familiar with Windows probably knows what to do.  Me?  When it doesn't catch right away I log out and back in.  That always does the trick.

``` text
PS > perl --version
This is perl 5, version 30, subversion 2 (v5.30.2) built for MSWin32-x86-multi-thread-64int

Copyright 1987-2020, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.
```

Now what about all the other package manger functionality?

## What about updating, listing, uninstalling, etc?

Um.  Well.  I mentioned `winget` is in preview, right?  Check the development [roadmap](https://github.com/microsoft/winget-cli/blob/master/doc/windows-package-manager-v1-roadmap.md).