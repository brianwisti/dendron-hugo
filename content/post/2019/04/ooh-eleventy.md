---
created: '2024-02-11 13:27:19'
date: 2019-04-06 00:00:00+00:00
description: ''
fname: pub.post.2019.04.ooh-eleventy
id: alrx86o5f05t8pgq4zi6921
slug: eleventy
syndication:
  mastodon: https://hackers.town/@randomgeek/101882459939490036
tags:
- node-js
- eleventy
- tools
title: Ooh Eleventy
updated: '2024-08-07 18:52:52'
---

Spring has sprung, and with it comes thoughts of new tools to build a Web site. Okay no the picture has nothing to do with Web sites but isn't it pretty?

<!--more-->

![flowers](assets/img/2019/cover-2019-04-06.jpg)

I use [Hugo]({{< relref "/card/hugo.md" >}}) to build this site, and have for *a while|pub.post.2015.09.next-hugo* now. Hugo builds fast, includes loads of features, and by now has the added benefit of being familiar. It's still fun to see what else people use for their sites, though.

*Eleventy* caught my eye with its claims at being a simpler static site generator. [Node.js]({{< relref "/card/node-js.md" >}}) powers Eleventy. That caught my attention because of how much I've been using the platform at work recently.

Aided by the [core documentation](https://www.11ty.io/docs/), I'll make a single page site with a stylesheet. To my mind, that's the ["Hello World"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) of static site generators. It covers the three core elements: content, layouts, and including files outside of the content/layout flow (stylesheets, images, etc).

> [!NOTE] What if you just want to blog?
> Use one of the [starter projects](https://www.11ty.io/docs/starter/), packaged with the configuration and plugins needed for blogging in Eleventy. I don't know enough about Eleventy or Node.js to tell you which one to use though!

## Starting fresh with `package.json`

I'll follow the [suggestion](https://www.11ty.io/docs/local-installation/) from docs and install Eleventy locally to the site project.

``` console
$ mkdir rgb-eleventy
$ cd rgb-eleventy
$ npm init
$ npm install --save-dev @11ty/eleventy
$ npx eleventy
Processed 0 files in 0.03 seconds
```

Yay, the process works! Now I need content.

## Content: Read Markdown, write HTML

I can stick with familiar [Markdown]({{< relref "/card/markdown.md" >}}) content, since Eleventy supports it through [markdown-it](https://markdown-it.github.io/). Throw a couple sentences in `index.md`:

``` markdown
# Random Geekery Blog

But in [Eleventy][].

[Eleventy]: https://www.11ty.io/
```

And rebuild the site.

``` shell
$ npx eleventy
Writing _site/index.html from ./index.md.
Processed 1 file in 0.07 seconds
```

So what's in `_site/index.html`?

``` html
<h1>Random Geekery Blog</h1>
<p>But in <a href="https://www.11ty.io/">Eleventy</a>.</p>
```

That's HTML, all right. But I need a full HTML page. Rather than make my content file more complex, I'll use a layout template.

## Templates

Eleventy [layouts](https://www.11ty.io/docs/layouts/) are similar to layouts in other site generators. They provide a skeletal HTML file along with special directives. These files get combined with your content files, creating complete pages that have a consistent layout and design.

Rather than focus on all the templating languages Eleventy supports, I'll use
[Nunjucks](https://mozilla.github.io/nunjucks/). I don't want to spend time looking at all the templating languages supported by Eleventy. I'll just use Nunjucks since it appears frequently in the docs.

My `_includes/layout.njk` is pretty much your basic minimal HTML 5 skeleton.

``` html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
  </head>
  <body>
    <h1>{{title}}</h1>

    {{ content | safe }}
  </body>
</html>
```

`content` comes from the body of the content file, while `title` is in `index.md`'s [front matter](https://www.11ty.io/docs/data-frontmatter/). That's also where I specify layout.

So yeah. I should probably add some front matter.

``` markdown
---
layout: layout.njk
title: Random Geekery Blog
---

But in [Eleventy][].

[Eleventy]: https://www.11ty.io/
```

Rebuild, and now `_site/index.html` looks like a Web page.

``` html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Geekery Blog</title>
  </head>
  <body>
    <h1>Random Geekery Blog</h1>

    <p>But in <a href="https://www.11ty.io/">Eleventy</a>.</p>

  </body>
</html>
```

## Use Pass-through File Copy for static content

Finally, I want to put in some CSS. I could just insert it in the template, but I prefer to keep styles in their own file.

Eleventy's default behavior is minimal. It knows content. It knows templates. Going beyond that requires special instructions. In order to add static content like stylesheets, we must [configure](https://www.11ty.io/docs/config/) Eleventy to recognize them.

My `.eleventy.js` tells Eleventy that everything in the folder `static/css` gets copied into site output unmodified.

``` javascript
module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("static/css");
    return {
        passthroughFileCopy: true
    };
}
```