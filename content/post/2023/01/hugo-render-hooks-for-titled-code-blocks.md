---
categories:
- post
created: '2024-02-10 17:41:16'
date: 2023-01-19
description: ''
fname: pub.post.2023.01.hugo-render-hooks-for-titled-code-blocks
id: kbqr5fs05x5i9l3ujfndj7s
syndication:
  linkedin: https://www.linkedin.com/posts/brianwisti_hugo-render-hooks-for-titled-code-blocks-activity-7022000696434556928-PSRJ
  mastodon: https://hackers.town/@randomgeek/109718751383178761
tags:
- hugo
title: Hugo Render Hooks for Titled Code Blocks
updated: '2024-08-25 18:26:54'
---

![titled code block](assets/img/2023/cover-2023-01-19.png "an illustrative example")

Captions more than titles, really. No problem. We'll fix it in post.

<!--more-->

I like to label my code blocks, especially when they describe the contents of a specific file.

That's been possible with [Hugo]({{< relref "/card/hugo.md" >}}) since 0.93.0, using [render hooks for code blocks](https://gohugo.io/templates/render-hooks/#render-hooks-for-code-blocks). Render hooks let you use custom templates for all instances of certain Markdown structures such as links, headers, images, and code! I didn't think to try them out for labeling code until just now, though. This [comment](https://discourse.gohugo.io/t/is-there-a-good-reason-not-to-have-a-mechanism-facilitating-a-title-for-code-blocks/40554/3) from Hugo Discourse user pamubay got me started. My template builds directly on theirs.

```html {title="layouts/_default/render-codeblock.html"}
{{- $isVerbatim := true -}}
{{- if isset .Attributes "verbatim" -}}
  {{- $isVerbatim = .Attributes.verbatim -}}
{{- end -}}
<figure class="highlight">
{{- with .Attributes.title }}
  <figcaption>
    {{- if $isVerbatim -}}
      <tt>{{ . }}</tt>
    {{- else -}}
      <span>{{ . }}</span>
    {{- end -}}
  </figcaption>
{{- end }}
{{- if transform.CanHighlight .Type }}
  <pre tabindex="0" class="chroma"
    ><code class="language-{{ .Type }}" data-lang="{{ .Type }}">
    {{- with transform.HighlightCodeBlock . -}}
      {{ .Inner }}
    {{- end -}}
  </code></pre>
{{- else }}
  <pre tabindex="0"
    ><code class="language-{{ .Type }}" data-lang="{{ .Type }}"
      >{{ .Inner }}</code></pre>
{{- end }}
</figure>
```

The HTML changes are personal aesthetics. I've been using `<figure/>` more and more often for illustrative examples beyond — you know — illustrations.

My render hook looks for two attributes, `title` and `verbatim`. These attributes are added after the language identifier for the fenced code block.

````markdown {title="Titled code block" verbatim=false collapsed=false}
```html{title="layouts/_default/render-codeblock.html"}
````

`title` is the intended title / caption to attach. The `verbatim` flag indicates whether I want this in a monospaced font. Grabbed that one from the Org folks since it seems like a useful differentiator between code and not-code.

Most of the time when I label code samples, I use a filename or identifier, and I'm used to seeing those in monospace. So it makes sense to have code block captions as verbatim by default. So the `verbatim` flag only matters if I set it to false, such as for explanatory captions.

````markdown { title="non-verbatim code block" verbatim=false collapsed=false}
```markdown{title="Titled code block" verbatim=false}
````

So now I can rest happily with Hugo now that it can do almost exactly what I — ooh [Pandoc 3.0](https://pandoc.org/releases.html#pandoc-3.0-2023-01-18) is out!