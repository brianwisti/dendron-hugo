---
created: '2024-02-17 21:10:12'
date: 2002-06-02 00:00:00+00:00
description: ''
fname: pub.post.2002.06.pagetemplate
id: 4fs4c77cd3uc3c6xdyuud2v
redirects:
- /coolnamehere/2002/06/02_pagetemplate.html
- /post/2002/pagetemplate/
- /2002/06/02/pagetemplate/
slug: pagetemplate
tags:
- pagetemplate
- coolnamehere
title: Pagetemplate
updated: '2024-08-07 18:22:32'
---

> [!WARNING]
> Haven't touched PageTemplate in ages. This stuff is only here for the historical record.

Archived repo: [brianwisti/PageTemplate A simple text templating system for Ruby](https://github.com/brianwisti/PageTemplate)

## Introduction

PageTemplate was a [Ruby]({{< relref "/card/ruby/_index.md" >}}) package which allowed you to utilize text templates for your Web projects. It was mainly intended for use in a CGI environment, but designed to be helpful in a broad range of similar applications. It was inspired by, yet almost entirely unlike, the [HTML::Template](http://html-template.sourceforge.net/) package available for Perl. It has many features in common with other templating engines:

- Variable substitution
- “if/else” blocks - inserting chunks of content depending on the existence of a flag variable
- “loop/no” blocks - repeatedly inserting a chunk of content, using values from a list
- Simple default syntax - *I hope it’s simple*

It also has a few features of its own (otherwise, where’s the fun?).

- Ruby-style access to fields and methods of objects
- Preprocessors to alter formatting of variables
- Support for defining values inside template
- Our Loops Are Crazy Fun:
  - Iteration over multiple loop variables
  - Named loop variables for easy-to-read object access
  - Loop meta-variables to simplify things like formatting alternate rows
- Customizable markup syntax to simplify integration with your own tools
  - Included `HTGlossary` for *HTML::Template* style syntax
- Cached templates for faster output

More features were planned, such as support for localization to allow native-language markup. But life had other demands, and I never did get back to PageTemplate.

Let's go back to 2002 present-tense verb usage while I decide what to do with these pages.

## What PageTemplate Is Not

- It’s not a programming language. If you want a programming language for your Web pages, try [PHP]({{< relref "/card/php.md" >}})
- It’s not a tool for embedding Ruby code into your Web pages. [ERB](http://ruby-doc.org/stdlib-2.4.1/libdoc/erb/rdoc/ERB.html) already does a fine job of that.
- It is *definitely* not XML. PageTemplate serves a much narrower field. If you want to use Ruby with XML, there are [excellent resources](http://www.rubyxml.org/) for that.
- PageTemplate is a personal project, which means that it’s not a commercial product. As much as I hope that it’s functional and stable on your computer, I can’t make any promises. If installing PageTemplate levels New Jersey, there’s nothing I can do about it. This is my version of the standard “no warranty” warranty.
- Last but not least, PageTemplate is not HTML::Template. HTML::Template has been growing and evolving for years, while PageTemplate was the result of a week alone with 5 pounds of coffee. Things have improved, but PT still suffers from the fact that it’s written and supported by two guys in their ever-dwindling spare time.

## Motivation

Brian has been a fan of Perl’s HTML::Template package for a long time, and he missed its robust usefulness whenever using a language that isn’t Perl. After delving deeper into other languages, he thought it might be fun to make some of that utility available in Ruby. It would give Brian a decent-sized personal project, which would stretch his skills with project development and unit testing. Plus, if a templating system was available, maybe he wouldn’t miss Perl so badly.

So those were the primary motivations: personal education and homesickness.

Once the code started taking shape, though, he decided that he wanted this to be useful for other people. “Download and use” kind of useful. Greg Millam found PageTemplate to be *so* useful that he opted to join in the development process and add loads of new features. PageTemplate has continued to be used by a small but apparently loyal group of people, despite Brian and Greg’s periodic hibernation. The continued contributions of Greg Millam have made PageTemplate a powerful tool for Web development rather than the mild distraction it started out as.

## Users

- [A Web-based library consult service for evidence-based medicine](http://www.pubmedcentral.nih.gov/articlerender.fcgi?artid=1484475)
  - We’re mentioned a ways down there, but they are using PageTemplate. If you have the keen eye required to read names in big letters near the top of the page, you’ll notice Greg was part of this team.
- [Weft QDA](http://www.pressure.to/qda/) - Text analysis? Sounds impressive. I’m guessing PageTemplate got used for exporting to HTML.