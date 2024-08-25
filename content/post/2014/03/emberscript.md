---
aliases:
- /tools/2014/03/26_emberscript.html
- /post/2014/emberscript/
- /2014/03/26/emberscript/
created: '2024-02-22 16:27:21'
date: 2014-03-26 00:00:00+00:00
description: ''
fname: pub.post.2014.03.emberscript
id: jgc13n2jb1taoz9pu5mppu8
slug: emberscript
tags:
- javascript
- tools
title: Emberscript
updated: '2024-08-07 18:39:46'
---

[Ember.js](http://emberjs.com/) is an impressive piece of [JavaScript]({{< relref "/card/javascript.md" >}}) work. It can also be painfully  verbose. A little syntactic sugar would make that go down easier. [EmberScript](http://emberscript.com/) is [CoffeeScript](http://coffeescript.org/) with fine-tuning specifically for Ember.js. Fine-tuning includes bits like replacing `class` and `extends` with `Ember.class` and `Ember.extends`.

<!--more-->

The simple example from the documentation:

``` coffeescript
class PostsController extends Ember.ArrayController
  trimmedPosts: ~>
    @content.slice(0, 3)
```

would expand out to

``` javascript
var PostsController;
var get$ = Ember.get;
PostsController = Ember.ArrayController.extend({
  trimmedPosts: Ember.computed(function () {
    return get$(this, 'content').slice(0, 3);
  }).property('content.@each')
});
```

Even if your team is using [RequireJS](http://requirejs.org/), it should look better than the vanilla JavaScript.

``` coffeescript
require [
  "lodash"
  "cs!models/PostModel"
], (_, PostModel) ->
  class PostsController extends Ember.ArrayController
    trimmedPosts: ~>
      # ...
      @content.slice(0, 3)
  return PostsController
```

The challenge is that in order to simplify the code we write, we've added layers between us and the code that the browser actually sees. CoffeeScript could interact weirdly with our dependencies, and EmberScript will undoubtedly have its own issues. Automated tests become even more important.

I need to think on this some more.