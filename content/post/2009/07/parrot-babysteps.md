---
aliases:
- /coolnamehere/2009/07/11_parrot-babysteps.html
- /post/2009/parrot-babysteps/
- /2009/07/10/parrot-babysteps/
created: '2024-02-10 16:09:28'
date: 2009-07-10 00:00:00+00:00
description: The introduction to Parrot Babysteps, my archived Parrot PIR tutorial.
fname: pub.post.2009.07.parrot-babysteps
id: yppvevmabyji7alyrj7m879
series:
- Parrot Babysteps
tags:
- parrot
- learn
- coolnamehere
title: Parrot Babysteps
updated: '2024-08-25 17:35:52'
---

## Introduction

I thought that maybe I could write a raw beginner's introduction to [Parrot]({{< relref "/card/parrot.md" >}}). This is a fair challenge, since coding directly for Parrot requires more work than using one of the languages that (2024 edit: was) written on top of the platform, such as [Raku]({{< relref "/card/raku.md" >}}). Still, my philosophy is that people shouldn't be afraid to dip their feet in new water, no matter how
cold or forbidding it may look.

## What?

[Parrot](http://parrot.org) is the name for the virtual machine that drives [Rakudo](http://rakudo.org) and [many other languages](http://www.parrot.org/languages). Part of the problem with writing programs has always been getting it to work on somebody else's machine. Sure, it's no problem if you're both using [Ubuntu](http://ubuntu.com), but what if you use Ubuntu and your friend uses Microsoft Windows? Of course, because it's been a problem for a long time there have been solutions for a long time as well. Python provides reasonable cross-platform standard libraries while still allowing you to "dive down" into operating system specifics.  As far as I can tell, [Perl]({{< relref "/card/perl.md" >}}) solves the problem by [pretending that everything is Unix](http://perldoc.perl.org/perlfork.html), but providing extensive libraries via the [CPAN](http://cpan.org) when you need to get at behavior that Perl can't just fake its way through.

Another solution that is becoming more popular is the [virtual machine](http://en.wikipedia.org/wiki/Virtual_machine) - more or less a pretend computer sitting on top of your own computer. Developers can all focus on writing code that works on the virtual machine, and the virtual machine - or "VM" - concerns itself with how to make the code work on *your* machine.

## Why?

Learning how to write directly for the Parrot VM could teach us a lot about how virtual machines work. PIR — the Parrot Internal Representation which is used when directly coding for Parrot — is an advanced language, but will still require that we spend time thinking about the details of what we want our code to do. This sounds more painful than it is, and using it could provide some enlightenment when trying to figure out how higher level languages such as Ruby, Perl, and Python work.

And besides that, learning new stuff is generally fun.

## Who?

I'm not a Parrot expert, and I don't expect you to be one either. The truth is that I barely know anything about Parrot. We are basically going to be learning how to write PIR code together. It would be nice if you know the basics of programming in another language, but not absolutely necessary.

If you *are* a Parrot expert, you may find my approach simplistic to the point of distraction. Please remember that my first focus when writing these is to help newcomers overcome their fear of an unfamiliar topic, and I will intentionally gloss over details that I suspect would increase that fear. Still, I don't want to share anything that's actually *wrong*. I will no doubt need pointers to better ways that a task can be accomplished, or to documentation that more clearly expresses a concept that I am trying to get across. I welcome your suggestions, and encourage you to contact me with your feedback.

## How?

Do you want to learn about Parrot? Go ahead! The [official documents](http://docs.parrot.org/parrot/latest/html/index.html) are the best place to get current and complete information, but I think that my own little foray into the platform
could help you get your feet wet.