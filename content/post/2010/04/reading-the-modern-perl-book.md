---
created: '2024-02-20 22:42:11'
date: 2010-04-06 00:00:00+00:00
description: ''
fname: pub.post.2010.04.reading-the-modern-perl-book
id: dzze9ib2tpjyhw1vgcd74kt
redirects:
- /blogspot/2010/04/06_reading-modern-perl-book.html
- /post/2010/reading-modern-perl-book/
- /2010/04/06/reading-the-modern-perl-book/
slug: reading-the-modern-perl-book
tags:
- perl
- blogspot
title: Reading the Modern Perl Book
updated: '2024-08-03 02:34:28'
---

I'm in the Perl phase of my language obsession rotation. I've created a handy
language obsession table you can use to simulate the behavior for your favorite
[GURPS][] Geek campaign.

[GURPS]: https://sjgames.com/gurps/

Roll 3d6 for the subject.

| Roll | Result |
| --- | --- |
| 3-6 | [Perl]({{< relref "/card/perl.md" >}}) |
| 7-9 | [Python]({{< relref "/card/python.md" >}}) |
| 10-11 | [Ruby]({{< relref "/card/ruby/_index.md" >}}) |
| 12-13 | [Parrot]({{< relref "/card/parrot.md" >}}) |
| 14 | [PHP]({{< relref "/card/php.md" >}}) |
| 15-18 | Something shiny I found on the Web. You can get plausible results by selecting a random entry from the [Wikipedia list of programming languages](http://en.wikipedia.org/wiki/List_of_programming_languages) |

Every week after the first, roll 1d6.

| Roll | Result |
| --- | --- |
| 1-3 | continue last week's language |
| 4-6 | roll on Table 1 for a new language |

Alternately, you can set a duration of 1d6 weeks. That's handy for an ADHD NPC
geek, where you don't want to check every week. Note that this is free time
obsession. The language at `$work` is whatever `$work` requires.

I don't know why I felt the need to share this. I've already spent more time on
that silly table than the actual subject I wanted to write about.

[Modern Perl blog]: https://modernperlbooks.com/mt/

So anyways - I'm messing about with Perl. I have been reading chromatic's
[Modern Perl blog][] for a while - even when I'm not in a Perl cycle. It's
good, you should try it out. He presents a needed perspective on Perl as
something more than a musty system administration language.

[draft]: https://github.com/chromatic/modern_perl_book

chromatic is also writing a book and maintaining the [draft][] on github. I
finally decided I wanted to read that draft. The README and a tiny bit of Git
knowledge provide all I need.

```sh
git clone git://github.com/chromatic/modern_perl_book.git
cd modern_perl_book
perl build/tools/build_chapters.pl
```

Now there is a handful of POD files in build/chapters which I could read with
perldoc.

```console
$ ls build/chapters
chapter_01.pod  chapter_03.pod  chapter_05.pod  chapter_07.pod  chapter_09.pod  chapter_11.pod  chapter_13.pod  chapter_15.pod
chapter_02.pod  chapter_04.pod  chapter_06.pod  chapter_08.pod  chapter_10.pod  chapter_12.pod  chapter_14.pod  chapter_16.pod
$ perldoc build/chapters/chapter_01.pod
```

I can also generate HTML for those days when perldoc just isn't making me
happy.

```console
$ perl build/tools/build_html.pl
Can't locate Pod/PseudoPod/HTML.pm in @INC (@INC contains: /usr/local/lib/perl5/5.10.1/darwin-2level /usr/local/lib/perl5/5.10.1 /usr/local/lib/perl5/site_perl/5.10.1/darwin-2level /usr/local/lib/perl5/site_perl/5.10.1 /usr/local/lib/perl5/site_perl .) at build/tools/build_html.pl line 6.
BEGIN failed--compilation aborted at build/tools/build_html.pl line 6.
```

Oops. It looks like there's a dependency. No problem.

```console
$ sudo cpan Pod::PseudoPod::HTML
$ perl build/tools/build_html.pl
$ ls build/html
chapter_01.html chapter_04.html chapter_07.html chapter_10.html chapter_13.html chapter_16.html
chapter_02.html chapter_05.html chapter_08.html chapter_11.html chapter_14.html style.css
chapter_03.html chapter_06.html chapter_09.html chapter_12.html chapter_15.html
```

Now I can open the chapters in my favorite Web browser.

```sh
elinks build/html/chapter_01.html
```

[tweets]: https://twitter.com/chromatic_x
[dents]: https://identi.ca/chromatic

From here, I can pay attention to chromatic's [tweets][] — or his [dents][],
since he seems more active on Identi.ca - or watch the `modern_perl_book`
repository on github. Whenever he mentions new content, I will refresh and
rebuild.

```sh
git pull
perl build/tools/build_chapters.pl
perl build/tools/build_html.pl
```

[Laziness]: https://c2.com/cgi/wiki?LazinessImpatienceHubris

I don't want to remember three whole commands. Am I taking [Laziness][] too
far? Perhaps. Nevertheless, here's a Perl script to handle the task. It should
only rebuild the chapters and HTML if there was an update in the repository.

```perl
#!/usr/bin/env perl
# refresh.pl

use Modern::Perl;

my $git_pull = `git pull`;

if ( $git_pull =~ m{\AAlready up-to-date.} ) {
    say "No changes to book.";
}
else {
    print $git_pull; # Show what updates were made.

    say "Building chapters.";
    system qw(perl build/tools/build_chapters.pl);

    say "Building HTML.";
    system qw(perl build/tools/build_html.pl);

    say "All done. Enjoy the update!";
}
```