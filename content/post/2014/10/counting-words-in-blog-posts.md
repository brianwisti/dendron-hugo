---
created: '2024-02-22 18:00:33'
date: 2014-10-02 00:00:00+00:00
description: Using Ruby to track my verbosity
fname: pub.post.2014.10.counting-words-in-blog-posts
id: z45ygonvy4csjtry7vlzope
redirects:
- /programming/2014/10/02_counting-words.html
- /post/2014/counting-words/
- /2014/10/02/counting-words-in-blog-posts/
slug: counting-words-in-blog-posts
tags:
- ruby
- programming
title: Counting Words in Blog Posts
updated: '2024-08-07 18:41:20'
---

I want to write at least 250 words per day. This is not a 30 day challenge. It is just something I want to do. I write more than 250 words daily when you count social network posts and chat text. Wouldn't it be nice if some of those words were organized around a single idea?
<!--more-->

I need some way to count those words, of course. The obvious solution is [wc](http://en.wikipedia.org/wiki/Wc_(Unix)).

```console
$ wc counting-words.markdown
     106     464    3108 counting-words.markdown
```

The documentation tells me that the first column is the number of lines, the second column is the number of words, and the third column is the number of characters. I can train my brain to remember this, but instead I use the `-w` flag to get *only* the word count.

```console
$ wc -w counting-words.markdown
     464 post.markdown
```

That is better, but it is not an accurate word count. I am currently using [Jekyll]({{< relref "/card/jekyll.md" >}}) for blogging, and every blog post file includes a section of [front matter](http://jekyllrb.com/docs/frontmatter/) a section of [Markdown]({{< relref "/card/markdown.md" >}}) content. My goal is 250 words of prose, not 250 total words. I do not want to count the front matter.

I could use assorted shell tools to accomplish this, but I would rather make a [Ruby]({{< relref "/card/ruby/_index.md" >}}) one-liner.

First I get the basic information I was already getting from `wc`.

```console
$ ruby -e 'puts ARGF.read.split.count' counting-words.markdown
464
```

How do I separate the head from the body of the post? I could do some fiddly bits using [ARGF.readlines](http://ruby-doc.org/core-2.1.3/ARGF.html#method-i-readlines) with a separator argument, but I will keep going with what I have.

```console
$ ruby -e 'puts ARGF.read.split(/^---$/).inspect' counting-words.markdown
["", "\nlayout: post\ntitle: Counting Words in Blog Posts\ndescription: Using Ruby to track my verbosity\ncategory: Programming\ndate: 2014-10-02\ntags: ruby\n", "\nI want to write at least 250 words per day. ..."]
```

How many words are in the body?

```console
$ ruby -e 'puts ARGF.read.split(/^---$/)[-1].split.count' counting-words.markdown
317
```

I did say that I wanted my word count to be prose. I should exclude code blocks. That calls for a multi-line regular expression, stripping out the fenced code blocks in my post.

```console
$ ruby -e 'puts ARGF.read.split(/^---$/)[-1].gsub(/^~~~ .+?^~~~ $/m, "").split.count' counting-words.markdown
357
```

I do not want to count link definitions either.

```console
$ ruby -e 'puts ARGF.read.split(/^---$/)[-1].gsub(/^~~~ .+?^~~~ |\[.+?\]:.+?$/m, "").split.count' counting-words.markdown
341
```

This is good enough. Now I turn it into a bash alias.

``` bash
# words in post / work in progress
alias wip='ruby -e '"'"'puts ARGF.read.split(/^---$/)[-1].gsub(/^(~~~ .+?^~~~ |\[.+?\]:.+?)$/m, "").split.count'"'"
```

Oh jeez those quotes hurt my brain. It was the first solution I came across to handle [shell quoting](http://stackoverflow.com/a/1250279/285810), though. I may come up with something prettier. Perhaps a full script or looking for an existing tool. This will do for now.

```console
$ wip counting-words.markdown
341
```

My one-liner ended up choking on some Markdown combinations, so I
turned it into a tiny script.

``` ruby
#!/usr/bin/env ruby

ignored_blocks = %r{
  (?: ^~~~ .+?^~~~ $)       # fenced code blocks
  |                         # or
  (?: ^\[ [^\]]+? \]: .+?$) # link definitions
}mx

puts ARGF.read.split(/^---$/)[-1].gsub(ignored_blocks, "").split.count
```

I needed that `/x` flag to make sense of my regular expressions.