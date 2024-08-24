---
created: '2024-02-11 19:49:29'
date: 2021-02-21 00:00:00+00:00
description: just a note, but too long to post as a note
fname: pub.post.2021.02.got-different-benchmarks-from-programming-crystal
id: qtu6l2ogywat2f5t0t0fr24
slug: got-different-benchmarks-from-programming-crystal
syndication:
  mastodon: https://hackers.town/@randomgeek/105773150089231524
tags:
- crystal
- benchmarking
- not-quite-errata
- programming
title: Got Different Benchmarks from Programming Crystal
updated: '2024-08-07 19:03:39'
---

Finally reading [Programming Crystal](https://pragprog.com/titles/crystal/programming-crystal/), by Ivo Balbaert and [Simon St.  Laurent](http://simonstl.com/).  Good stuff.  The [Crystal]({{< relref "/card/crystal.md" >}}) language has advanced some since the book came out, but nearly all the code runs as-is.

Something that jumped out at me was the difference between their results and mine with the [benchmarking](https://github.com/Ivo-Balbaert/programming_crystal/blob/master/code/managing_projects/benchmarking.cr) example.  Not the raw numbers.  I'd be a little confused if those were exactly the same.  The ratios caught my attention.

Given this source:

```crystal
require "benchmark"

IOM = IO::Memory.new

Benchmark.ips do |x|
  x.report("Appending") do
    append
    IOM.clear
  end

  x.report("Using to_s") do
    to_s
    IOM.clear
  end

  x.report("Interpolation") do
    interpolation
    IOM.clear
  end
end

def append
  IOM << 42
end

def to_s
  IOM << 42.to_s
end

def interpolation
  IOM << "#{42}"
end
```

Here's what we're told to expect.

> Build the code for production using `$ crystal build benchmarking.cr —release` and execute that with: `$ ./benchmarking`
>
> You’ll get results like this:
>
> ```plaintext
> Appending    34.06M ( 29.36ns) (± 3.97%) fastest
> Using to_s   12.67M ( 78.92ns) (± 7.55%) 2.69× slower
> Interpolation  2.8M (356.75ns) (± 3.84%) 12.15× slower
> ```

But in Crystal 0.36.1 on Ubuntu 20.04, running on Windows WSL2:

```plaintext
$ ./benchmarking
    Appending 110.36M (  9.06ns) (± 3.70%)   0.0B/op        fastest
   Using to_s  18.52M ( 54.00ns) (± 5.36%)  16.0B/op   5.96× slower
Interpolation  19.19M ( 52.12ns) (± 2.99%)  16.0B/op   5.75× slower
```

Sure, my numbers are bigger than the book's.  That's cool.  But `interpolation` and `to_s` are so close to each other on my machine!

Maybe that's WSL?  After I get the day's tasks done, I revisit on my computer's Manjaro partition.

```plaintext
$ ./benchmarking
    Appending 123.54M (  8.09ns) (± 2.57%)   0.0B/op        fastest
   Using to_s  56.57M ( 17.68ns) (± 3.49%)  16.0B/op   2.18× slower
Interpolation  56.55M ( 17.68ns) (± 4.32%)  16.0B/op   2.18× slower
```

Well heck.

It's faster on native Linux than WSL.  That's hardly surprising.  But the differences between `to_s` and `interpolation` are now negligible.  For that matter, both of them are closer to the speed of `append` than `to_s` was in the book's example!

Is the difference because of changes in Crystal?  Some dependency, like LLVM? My computer's 40GB of RAM compared to whatever the authors used?  My hard drive?  GPU?  Is Mercury in retrograde?

*I don't know!* I just saw different numbers and thought it was curious.

My point isn't that the book's wrong.  Heck no.  The example's supposed to remind you that testing your assumptions is important.  All I've done is emphasized the validity of the lesson.

Anyways.

Good book.  Fun language.  Don't forget to try out the example code.  And if you need to care about performance?  Don't assume — benchmark.