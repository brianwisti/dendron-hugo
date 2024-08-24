---
created: '2024-02-20 05:24:07'
date: 2009-09-21 00:00:00+00:00
description: ''
fname: pub.post.2009.09.perl-hacks-in-my-workspace
id: yruv0utivv2h7hvauykollh
redirects:
- /coolnamehere/2009/09/21_perl-hacks-in-my-workspace.html
- /post/2009/perl-hacks-in-my-workspace/
- /2009/09/21/perl-hacks-in-my-workspace/
slug: perl-hacks-in-my-workspace
tags:
- perl
- coolnamehere
title: Perl Hacks in My Workspace
updated: '2024-08-07 18:36:50'
---

Looking at some specific hacks from the O'Reilly [Perl Hacks](http://oreilly.com/catalog/9780596526740/) book for my own [Perl]({{< relref "/card/perl.md" >}}) workflow. It should be obvious from the tone and content that this is not intended to replace any of the  original material or take credit for anything in the book.

<!--more-->

Perl Hacks is a great book. I catch something new every time I open it. That's
at least partly because I still haven't read it from cover to cover. The "Hacks"
series of books is written in such a way that cover-to-cover reading is not
needed, thankfully.

The browser hacks from the beginning are an especially convenient way
to add some Perl-friendly functionality to Firefox.
One minor issue is that I spend a lot of my time in [ELinks](http://elinks.cz/),
a text-based Web browser. Why? Well, most of my work is done over an ssh
connection, so I'm already using GNU screen and Vim. Keeping my Web
browser within my `screen` session reduces context switching. `screen` also
keeps my sessions alive, so everything including my ELinks browser session is
intact when I come back to my workspace the next morning.

Naturally, I had to examine Hack #1 in the context of ELinks.

## Hack #1: Add CPAN Shortcuts to ELinks

There are a couple of preliminary steps to get out of the way before adding
CPAN shortcuts to ELinks. First, install ELinks. Second, make sure smart
prefixes are enabled.

### Installing ELinks

The first requirement for this hack is ELinks. The [ELinks download page](http://elinks.cz/download.html) shows all sorts of nifty ways to install it. I went the easy way and just used my system package managers.

That's `apt-get` on [Ubuntu](http://www.ubuntu.com) Linux:

    sudo apt-get install elinks

Or [MacPorts](http://www.macports.org/) on OS X:

    sudo port install elinks

Windows folks are left to their own devices, since most of my Windows `elinks`  usage is on other systems via [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/). I do know that ELinks is available in [Cygwin]({{< relref "/post/2004/07/cygwin.md" >}}).

### Enable Smart Prefixes

The easiest way to test if smart prefixes are enabled is by trying to use
one that's already been defined. Try opening the following URL in ELinks:

    g Modern::Perl

The resulting page should look something like [this](http://www.google.com/search?q=Modern%3a%3aPerl&btnG=Google+Search).
Follow these steps if that is not the case:

* Enter `o` to open the Options Manager
* Open Protocols / URI Rewriting / Enable Smart Prefixes
** Use the space bar to expand the tree as you go.
* Select `[Edit]`
* Make sure the text field is set to `1`.
* Select `[OK]`
* Select `[Save]`

Now go back and try to open `g Modern::Perl` again. That did the trick for me.

On to the CPAN shortcuts.

### Adding a Smart Prefix

* Enter `o` to open the Options Manager
* Open Protocols / URI Rewriting / Smart Prefixes
  * Use the space bar to expand the tree as you go.
* Select `[Add]`
* Enter the name of the smart prefix, then select `[OK]`
* Select `[Edit]`
* Enter the URL for the smart prefix, then select `[OK]`
* Select `[Save]`

### The Smart Prefixes

Description                   | Prefix | URL
------------------------------|--------|-------------------------------------------------------------------
Search CPAN                   | cpan   | `http://search.cpan.org/search?mode=module;query=%s`
Show Module Documentation     | cpod   | `http://search.cpan.org/perldoc/%s`
AnnoCPAN Module Documentation | apod   | `http://www.annocpan.org/?mode=search;field=Module;latest=1;name=%s`

### Try Them Out

Try the following URLs to get you started.

* `cpan Modern::Perl`
* `cpod Acme::Python`
* `apod Moose`

## References

* [Perl Hacks](http://oreilly.com/catalog/9780596526740/) by chromatic with
  Damian Conway and Curtis 'Ovid' Poe. Copyright 2006 O'Reilly Media, Inc., 0-596-52674-1