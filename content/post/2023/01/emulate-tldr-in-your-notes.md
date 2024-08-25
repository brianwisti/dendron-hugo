---
categories:
- note
created: '2024-02-10 17:42:48'
date: 2023-01-31 00:00:00+00:00
description: ''
fname: pub.post.2023.01.emulate-tldr-in-your-notes
id: 5htdyfg93as1xp423c01dgs
slug: emulate-tldr-in-your-notes
syndication:
  linkedin: https://www.linkedin.com/posts/brianwisti_logseq-secondbrain-blog-activity-7026211616236982272-jRco
  mastodon: https://hackers.town/@randomgeek/109784550162499793
tags:
- logseq
- second-brain
title: Emulate tldr instead of man in your notes
updated: '2024-08-25 18:27:06'
---

![annotated logseq bullet point](assets/img/2023/cover-2023-01-31.png "A bullet point is a note given the right tag")

[Tldr]({{< relref "/card/tldr.md" >}}): Emulate [`tldr`](https://tldr.ostera.io/tar) instead of [`man`](https://man7.org/linux/man-pages/man1/tar.1.html) in your notes.

I still use my PKMs wrong. Keep your notes small. Stick with one tool. Stay focused. Yep, none of that.

But I *have* learned that emulating man page style isn't great. I have big notes on commands with every option, every subcommand, and every subcommand's option.

Then I'd end up searching online how to do a thing. Because I wasn't using a searchable style.

Few months ago I had a moment of enlightenment. Most of what I want in my knowledge garden is to track *processes* — how to do a specific thing. Why not make the notes reflect that?

Use clear language directly relevant to the task at hand. Tag them appropriately with a key tag like "process". You do end up with a lot of notes — or a lot of bullet points, if you use an outliner like [Logseq]({{< relref "/card/logseq.md" >}}).

````markdown
- Use Rclone to pull *from* a Dropbox folder #process
 - ```sh
   rclone sync dropbox:Settings ~/Dropbox/Settings
   ```
- Use Rclone to push *to* a Dropbox folder #process
 - ```sh
   rclone sync ~/Dropbox/Settings dropbox:Settings
   ```
````

But they will be easier to find a few months later when all you can remember is "something something [Rclone](https://rclone.org/) something [Dropbox](https://dropbox.com/)".

![Logseq search results with example bullets at top of the list](assets/img/2023/2023-01-31-rclone-search.png "There it is!")

I had these particular processes in the main page for Rclone, but most are scattered throughout my journal pages. It makes no difference, since I use the tag consistently.