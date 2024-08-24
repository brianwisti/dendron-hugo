---
created: '2024-02-11 13:14:42'
date: 2022-01-03 00:00:00+00:00
description: something something "right tool for the right job"
fname: pub.post.2022.01.building-my-eleventy-site
id: nn1ae1nkijtzlxin04ezdrv
redirects:
- /note/2022/01/building-my-eleventy-site/
slug: building-my-eleventy-site
syndication:
  mastodon: https://hackers.town/@randomgeek/107562930844947425
tags:
- eleventy
- node-js
- site
title: Building My Eleventy Site
updated: '2024-08-07 19:08:23'
---

![a wooden mixing spoon snapped into two over a recipe book](assets/img/2022/cover-2022-01-03.jpg "sometimes the tools break")

Not a huge post. I'm using this [Eleventy]({{< relref "/card/eleventy.md" >}}) incarnation of the site as a way to learn a few [Node.js]({{< relref "/card/node-js.md" >}}) topics, and many of those concepts are still sinking in.

## So how am I building this thing?

We know it's Eleventy. But what did I find to get a decent web nerd workflow?

Let's go down the list. You may know better choices. I won't complain if you share them nicely.

You may *not* know better choices. If you come wandering in from some search engine, *this page is not expert opinion.* It's just what I was able to find that could glue everything together long enough to publish a site.

So let's go down the list.

### `yarn` to run everything

I opted to drive this with [Yarn](https://yarnpkg.com.) For my beginner brain it looks equivalent to [npm](https://docs.npmjs.com/cli/v8) but I find Yarn's usage and invocation more pleasant.

### `package.json` to tell Yarn what I want it to do

Everybody seems to treat the [`scripts`](https://docs.npmjs.com/cli/v8/configuring-npm/package-json#scripts) block of a [`package.json`](https://docs.npmjs.com/cli/v8/configuring-npm/package-json) pretty
much the same as the targets of a `Makefile` so I embraced that.

Here are my core scripts / tasks:

```json
{
  "scripts": {
    "dev": "npm-run-all --parallel serve watch:style",
    "build:dev": "npm-run-all --serial site:img site:style site:content",
    "build:prod": "npm-run-all --serial site:img site:style site:content:prod",
    "clean": "rimraf dist",
    "push": "rsync -av dist/ vps:randomgeekery.org",
    "serve": "eleventy --serve --quiet",
    "site:img": "ts-node build_tasks/process_images.ts",
    "site:content": "eleventy --quiet",
    "site:content:prod": "INCLUDE_ANALYTICS=1 eleventy --quiet",
    "site:style": "sass ./src/assets/scss/main.scss ./dist/assets/css/main.css",
    "watch:style": "sass --watch ./src/assets/scss/main.scss ./dist/assets/css/main.css"
  }
}
```

Build, develop, clean, upload. All the basics are there. I don't think `package.json` *really* has namespaces, but I use `:` to pretend.

> [!NOTE]
> I have a few more entries but until I smooth them out a bit they'll just add noise. I left them out for now.
>
> `site:img` is part of that noise to be honest, but it's mentioned prominently in other entries. Basically I preprocess my images with [eleventy-img](https://www.11ty.dev/docs/plugins/image/). We'll talk more about that another day maybe.

### `ts-node` to execute TypeScript code

In the process of learning [TypeScript]({{< relref "/card/typescript.md" >}}), and I'm very much a "learn by doing" sort of person. "Doing" here means "typing the code and making it run." I'll learn the compilation framework of `tsc` soon enough, but [ts-node](https://typestrong.org/ts-node/) lets me execute my TypeScript code immediately.

I like that.

### `sass` to make things pretty — eventually

I'm sure I'll get deeper into [Tailwind](https://tailwindcss.com) or [Windi](https://windicss.org) eventually, but for now it's still easier to write my styles in [Sass](https://sass-lang.com).

And yes I know my styles are rough right now. Decided if I let myself linger and wait for the perfect layout I'd never push the update. But I'll get to it.

### `npm-run-all` so I can do *two* things with *one* command

The only thing I couldn't figure out how to do with `package.json` was run two tasks with a single command. That's apparently because it doesn't do that on its own. `package.json` is not a `Makefile`.

Have no fear. [`npm-run-all`](https://github.com/mysticatea/npm-run-all) is here. It's a CLI application focused on letting you run multiple `package.json` script commands, sequentially or in parallel.

### `rsync` to share it when I'm ready

This is a static site served by [Apache](https://httpd.apache.org). It doesn't need some continuous integration / deployment pipeline. I have files. [rsync](https://rsync.samba.org) uploads them with a quickness.

`rsync` has been part of my toolkit for years. I'll replace it when I don't need it anymore.

### `rimraf` to clean up after myself

Everyone else is using [`rimraf`](https://github.com/isaacs/rimraf) to clean build and intermediate files. I don't know enough to choose any different.

## That's all the important stuff anyways

I wanted to go over everything, but there's just too much. A lot of the ideas are still cooking. Expect more on every blogger's favorite topic: "how I built my blog."

I'm having fun though!