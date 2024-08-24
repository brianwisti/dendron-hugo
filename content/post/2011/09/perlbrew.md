---
created: '2024-02-22 14:11:46'
date: 2011-09-05 00:00:00+00:00
description: ''
fname: pub.post.2011.09.perlbrew
id: k6xfo7lkc091l0iapssy54x
redirects:
- /coolnamehere/2011/09/05_perlbrew.html
- /post/2011/perlbrew/
- /2011/09/05/perlbrew/
slug: perlbrew
tags:
- perl
- coolnamehere
title: Perlbrew
updated: '2024-08-07 18:39:10'
---

::: tip TL;DR:

```bash
curl -L http://xrl.us/perlbrewinstall | bash
perlbrew init
perlbrew install perl-5.14.2
perlbrew switch perl-5.14.2
```

:::

## Introduction

You probably already have [Perl]({{< relref "/card/perl.md" >}}) if you are running Linux or OS X. However, it is usually not the latest version of the language. I prefer to install my own copy. That way I can take advantage of new language  features. Also, the system Perl is often used in administrative scripts. There is always the chance that my experiments will mess something up. It is not easy, but I have done it before.

Fortunately, there's [perlbrew](https://perlbrew.pl/). perlbrew allows you to install your own personal Perl, which doesn't interfere with other installed versions. Speaking of versions: `perlbrew` lets you install and switch between multiple personal Perls. When Perl 5.16 is released, upgrading will be handled by a couple of quick commands.

Not interested in reading my rambling article? That's okay. Make sure you have your operating system's build tools first.

## Installing Perlbrew

There are a couple of ways to install perlbrew. Some of them only
apply to specific platforms, while one should work on any UNIX-like
operating system.

Fortunately, all of the installation techniques are simple.

### Linux Packages

Fresh releases of some Linux distributions have perlbrew available as a package. I only know of a couple right now, but I will expand this if I learn of more.

#### Installing `perlbrew` on Fedora Linux

Current versions of [Fedora Linux](http://fedoraproject.org) already have `perlbrew` available via [`yum`](http://fedoraproject.org/wiki/Yum).

```console
$ su -
# yum install perlbrew
```

#### Installing `perlbrew` on Ubuntu 11.10

If you're on the bleeding edge of Ubuntu development, or are reading  this after October 2011, you'll be happy to know that there is an [Ubuntu 11.10 perlbrew package](https://launchpad.net/ubuntu/oneiric/+package/perlbrew).

Ubuntu 11.10 or later only!

```bash
sudo apt-get install perlbrew
```

#### Installing `perlbrew` on other UNIX-like systems

You will want to have a minimal development environment before you install `perlbrew`.

#### Ubuntu

The `build-essentials` package provides the basic command line tools you will need to build and install Perl via `perlbrew`.

```bash
sudo apt-get install build-essentials
```

Once `build-essentials` has been installed, you can install `perlbrew`.

```bash
curl -L http://xrl.us/perlbrewinstall | bash
```

#### OS X

Install [Xcode](https://developer.apple.com/xcode/). It's a simple step, but tends to take a while. Xcode is actually a huge Integrated Development environment. You can try [gcc without Xcode](https://github.com/sorin-ionescu/gcc-without-xcode) if you're not interested in the IDE. I have not tested it yet. I just know that it exists.

Once you have your development tools installed via Xcode, run the following command from a Terminal.

```bash
curl -L http://xrl.us/perlbrewinstall | bash
```

The official perlbrew page and the [App::perlbrew documentation](https://metacpan.org/module/App::perlbrew) should help you get the details about fiddly bits of installing `perlbrew`.

### Initializing Perlbrew

Regardless of how you installed perlbrew, now you will want to make sure it is set up for your account.

```bash
perlbrew init
```

You will get directions on the next step. It will probably be something like this:

Make sure you have something like the following line at the end of your  shell profile. That's `~/.bashrc` for me.

``` bash
source /Users/brian/perl5/perlbrew/etc/bashrc
```

Reload your settings either by opening a new Terminal or directly from
the shell:

```bash
. ~/.bashrc
```

Now you are ready to install your own Perl.

## Using `perlbrew` To Install Perl

It's probably a good idea to see what Perl versions are available to  install.

```console
$ perlbrew available
   perl-5.15.3
   perl-5.14.2
   perl-5.12.4
   i perl-5.10.1
   perl-5.8.9
   perl-5.6.2
   perl5.005_04
   perl5.004_05
   perl5.003_07
```

We're looking for the latest stable release. Stable releases use an even number for the second number (`perl-5.14.2`, `perl-5.12.4`). The development releases (`perl-5.15.3`) probably will not interest you unless you are curious about features and fixes that are being experimented with for the next stable Perl. It is very rare that I install a development Perl.

Right now, the latest stable Perl is `perl-5.14.2`. Let's install it with `perlbrew install`.

```bash
perlbrew install perl-5.14.2
```

A little while later, it'll be complete. You can make this the default Perl for your account with `perlbrew switch`.

```bash
perlbrew switch perl-5.14.2
```

Let's verify just to be on the safe side.

```bash
$ perl --version
This is perl 5, version 14, subversion 2 (v5.14.2) built for darwin-2level
```

There. Now we have the latest stable Perl, ready for us to use. The system Perl is completely safe.

As far as I can tell, there is no official way to carry installed Perl modules over to a new Perl installed via perlbrew. You can set the `$PERL5LIB` environment variable or rely on `use lib` if it's important to use specific installed libraries.