---
created: '2024-02-23 13:37:51'
date: 2015-09-14 00:00:00+00:00
description: '''I started writing about PNWPHP but got distracted and added "Suggested
  Reading" to my posts instead.''

  '
fname: pub.post.2015.09.added-suggested-posts
id: k67taq8pk323jz229yljszo
redirects:
- /tools/2015/09/14_adding-suggested-posts.html
- /post/2015/adding-suggested-posts/
- /2015/09/14/added-suggested-posts/
slug: added-suggested-posts
tags:
- jekyll
- site
- tools
title: Added Suggested Posts
updated: '2024-08-07 18:44:33'
---

I started writing about [PNWPHP](http://www.pnwphp.com/) but got distracted and added "Suggested Reading" to my posts instead.

<!--more-->

This weekend I attended PNWPHP. It was great. Instead of writing about that, I started looking up how to manage Related Posts in [Jekyll]({{< relref "/card/jekyll.md" >}}). There are built-in options to do that, but they never satisfied me. I found [Wenli Zhang](http://zhangwenli.com/)'s post "[Jekyll Related Posts without Plugin](http://zhangwenli.com/blog/2014/07/15/jekyll-related-posts-without-plugin/)" and understood a little better.

Okay, no. Not really. But that post led me to [related_posts-jekyll-plugin](https://github.com/LawrenceWoodman/related_posts-jekyll_plugin) and this [fork by jumanji27](https://github.com/jumanji27/related_posts-jekyll_plugin) which is friendlier for current Jekyll releases.

Since it's a little more fiddly than a regular plugin, I hand-copied the code into a file `_plugins/related-posts.rb` and added a nice little "Suggested Posts" footer to the post template.

``` handlebars
<article itemscope itemtype="http://schema.org/BlogPosting">
  ...
  <footer>
    <h3>Suggested Posts</h3>
    <p>
      {% for post in site.related_posts limit:5 %}
      <a href="{{ post.url }}" class="post-link">{{ post.title }}</a>{% unless forloop.last %}, {% endunless %}
      {% endfor %}
    </p>
  </footer>
</article>
```

I limited it to five related posts. Some posts will have a hundred related posts due to the way I imported content from my other sites.

Incidentally, I think this plugin does a better job picking related posts than Jekyll's built-in approach, though I have no idea why. Jekyll usually ended up with nothing related, and just defaulted back to the most recent posts. This works better for me.

For the moment I prefer a comma-delimited dump of posts. Later I may play with some list styling. However, I did have the problem of post titles being broken up by line breaks. A little `white-space: nowrap` in the right spot fixes that.

``` css
a.post-link {
  white-space: nowrap;
}
```

Now the text of each post link stays together.

Just wanted to share all this. Have fun!