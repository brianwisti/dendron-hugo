---
aliases:
- /post/2018/06/buy-my-stuff-at-design-by-humans/
category: post
created: '2024-03-06 14:36:57'
date: 2018-06-12 00:00:00+00:00
description: ''
fname: pub.post.2018.06.buy-my-stuff-at-design-by-humans
id: 0vesrmhvediqy3xsjogg0fa
slug: buy-my-stuff-at-design-by-humans
tags:
- drawing
- infinite-painter
- hugo
- buy-me
- craft
title: Buy My Stuff at Design by Humans
updated: '2024-03-06 14:59:55'
---

![purple mandala-style symmetry drawing](assets/img/2018/cover-2018-06-12.png)

Well, one design. I only got things going yesterday, with a quick sketch on a plain white background. Future plans include adjusting old designs and creating new ones for the store, with an intended pace of roughly one design per week.

Of course I already worked out the site integration. Everything on Random Geekery tagged "buy me" should have a direct link to its page on the store. I get a lovely Hugo [`errorf`](http://gohugo.io/functions/errorf/) message if I forget the link.

```plaintext
{{- if in .Params.tags "buy me" -}}
  {{- if isset .Params "purchase" -}}
    {{- with .Params.purchase -}}
      <p class="cover-link">
        <a href="{{ .url }}" target="_blank">{{ .caption }}</a>
      </p>
    {{- end -}}
  {{- else -}}
    {{ errorf "%s Tagged 'buy me' without purchase front matter!" .File.Path }}
  {{- end -}}
{{- end -}}
```

My partial is a little clunky, but it worked. I can improve it later.