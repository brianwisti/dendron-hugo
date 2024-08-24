---
created: '2024-02-22 17:32:16'
date: 2014-06-25 00:00:00+00:00
description: ''
fname: pub.post.2014.06.perl-520-signatures-in-subroutine-references
id: dkzqlfvpux6gm58edpt28ng
redirects:
- /programming/2014/06/25_perl-subref-signatures.html
- /post/2014/perl-subref-signatures/
- /2014/06/25/perl-5.20-signatures-in-subroutine-references/
slug: perl-520-signatures-in-subroutine-references
tags:
- perl
- programming
title: Perl 5.20 Signatures in Subroutine References
updated: '2024-08-07 18:40:30'
---

[Perl]({{< relref "/card/perl.md" >}}) 5.20 has experimental support for function signatures. That's  good news. I just thought to check if signatures can be used in subroutine references. They can.

<!--more-->

``` perl
# Set a base set of features.
use 5.20.0;

# Signatures are experimental, so are not enabled by default.
use feature 'signatures';

# Otherwise Perl will warn about using the experimental feature
no warnings 'experimental::signatures';

sub hello($person) {
  say "Hello, $person";
}

my $goodbye = sub($person) {
  say "Goodbye, $person";
};

my $me = "Brian";

hello( $me );
$goodbye->( $me );
```

It's a simple test. Just checking to see if I can maybe use this feature in my own projects.

``` console
$ perl sig-test.pl
Hello, Brian
Goodbye, Brian
```

This pleases me. It's not going to make life easier for [Pygments](http://pygments.org/), though.