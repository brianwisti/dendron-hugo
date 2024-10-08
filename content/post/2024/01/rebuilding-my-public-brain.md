---
categories:
- post
created: '2024-02-10 14:35:29'
date: '2024-01-22T00:00:00.000Z'
description: ''
fname: pub.post.2024.01.rebuilding-my-public-brain
id: vpyoh03q8v3tlg7f5p3rmjt
slug: rebuilding-my-second-brain
summary: I changed my blogging workflow — again.
syndication:
  mastodon: https://hackers.town/@randomgeek/111801976876465759
tags:
- site
- second-brain
title: Rebuilding My Public Brain
updated: '2024-08-25 18:19:18'
---

## What?

I took all my blog posts since 2000 — since before the site was a blog — put them in [Obsidian]({{< relref "/card/obsidian.md" >}}), extracted note cards for recurring content, and smashed the whole thing into a new iteration of [Random Geekery]({{< relref "/card/random-geekery.md" >}}).

## Why?

I tried sharing [My Public Brain]({{< relref "/card/my-public-brain.md" >}}) a couple times. It didn't work out. Maintaining an extra site added personal friction, and I ended up ignoring all of it. I wanted to keep trying, though. My first site [Coolnamehere]({{< relref "/card/coolnamehere.md" >}}) was an organized collection of notes on topics as I learned them. I've mostly been blogging the last decade, but missed the ability to link back to topic notes from my posts.

At the very least, having dedicated topic cards means fewer places to update external links. That can save a few minutes of effort over a couple decades, for sure.

Storing the whole thing in a [PKM]({{< relref "/card/pkm.md" >}}) makes it easier to find mentions and follow cross-references, eventually ensuring some kind of consistency in site structure.

## Okay, How?

### Building the vault

Most of the details and reasoning are over where I describe [How These Notes Are Organized]({{< relref "/card/how-these-notes-are-organized.md" >}}). Basically I have a private folder for new notes, a private folder for journaling, and a private folder for vault templates. Everything else is public.

The process itself was manual:

- drop all the Markdown from my Hugo site into `post/`
- arrange posts by year and month so they match permalink expectations, cleaning up and extracting (laughably minimal) new notes for recurring topics as I go; sometimes a post no longer has even personal historical relevance, so I remove it
- periodically review those new notes, maybe flesh them out a little bit, and move them to public `card/`
- Drop in my config files, clean them up a tiny bit, and pinky-promise I'll do more with them later

This process of evaluation and refactoring was fundamentally manual, so I limited the plugins to what I needed to mark progress and visually distinguish links.

- [Link Favicons](https://github.com/joethei/obsidian-link-favicon) visually identifies external links
- [Plugin Update Tracker](https://github.com/swar8080/obsidian-plugin-update-tracker) so I can keep up with current plugins without extra mental effort
- [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links) so I can declare link types for each of my major note sections
- [Style Settings](https://github.com/mgmeyers/obsidian-style-settings) to define visual design elements for the link types I defined in Supercharged Links
- [Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title) because sometimes link titles are hard; just use the existing site title and edit if confused
- [Calendar](https://github.com/liamcain/obsidian-calendar-plugin) because it's still a PKM and that means daily journal notes; this plugin makes it easier to get at past journals.
- [Tag Wrangler](https://github.com/pjeby/tag-wrangler) because I'm going to need help cleaning up all those blog post tags
- [Vault Statistics](https://github.com/bkyle/obsidian-vault-statistics-plugin) to see ~~my score~~ how many pages I have in this vault

I'll probably add plugins later, but the extra functionality of Templater or Dataview would have distracted me from the core task. It happened with previous note consolidation efforts.

### Building the site

Initially I pulled the vault into an [Astro]({{< relref "/card/astro.md" >}}) site with  [ts-node](https://typestrong.org/ts-node/). It sort of worked. Came into some issues with `ts-node` on very fresh [Node.js]({{< relref "/card/node-js.md" >}}) though, and decided to see if someone had already figured out Obsidian export.

Turns out, yes. [obsidian-export]({{< relref "/card/obsidian-export.md" >}}) handles internal links and provides some starter template logic for working with [Hugo]({{< relref "/card/hugo.md" >}}). I'm setting Astro aside for the moment. Sticking with Hugo made cleanup easier, since I no longer had to care about shortcodes.

Got a Perl script for backlinks and a Python script for processing Obsidian Markdown rules that `obsidian-export` didn't cover. Not happy with either of those scripts yet, so I won't go into detail about them here. The Perl script finds backlinks and puts them in a data file for quicker backlink handling at site build time, and the Python script currently does some regular expression handling to identify special markup and transform it.

I pulled in my automated tests from the current site iteration. I really should talk more about those tests at some point. They mostly check for structural issues with `markdownlint` and broken internal links.

## What next

Before I have the Python script handle all the processing, I'll revisit the Astro iteration. [remark-obsidian](https://www.npmjs.com/package/remark-obsidian) and [remark-deflist](https://www.npmjs.com/package/remark-definition-list) handled nearly all the special Markdown for me. I mainly need to decide how top-level pages like [Now]({{< relref "/slash/now.md" >}}) and [Follow]({{< relref "/slash/follow.md" >}}) get treated within Astro's dynamic collection approach.

## What now

Budget is constrained, so before the annual hosting bill comes due I'll shift from a paid host to Netlify. My planned usage tier should be free there. I expect to bounce back out again after resolving the current [Job Search]({{< relref "/card/job-search.md" >}}) to my satisfaction, but maybe not. We'll see.

Hugo works. Netlify works. My notes need work, but hey don't we all. I'm not going to jiggle anything else just yet.

I think it's time for `just pull backlinks process build test push`.

Hm.

Maybe tighten that invocation up just a little bit.