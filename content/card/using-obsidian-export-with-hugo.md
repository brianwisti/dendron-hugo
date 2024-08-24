---
created: '2024-02-10 04:41:35'
description: ''
fname: pub.card.using-obsidian-export-with-hugo
id: kudkp16q87ym515z0tnu65p
title: Using Obsidian Export with Hugo
updated: '2024-02-10 04:41:59'
---

Copied directly from the [obsidian-export]({{< relref "/card/obsidian-export.md" >}}) REAME

## Transforming links

Turns `../../Card/ADHD.md` to `/card/adhd`.

```go-html-template {title="layouts/_default/_markup/render-link.html"}
{{- $url := urls.Parse .Destination -}}
{{- $scheme := $url.Scheme -}}

<a href="
  {{- if eq $scheme "" -}}
    {{- if strings.HasSuffix $url.Path ".md" -}}
      {{- relref .Page .Destination | safeURL -}}
    {{- else -}}
      {{- .Destination | safeURL -}}
    {{- end -}}
  {{- else -}}
    {{- .Destination | safeURL -}}
  {{- end -}}"
  {{- with .Title }} title="{{ . | safeHTML }}"{{- end -}}>
  {{- .Text | safeHTML -}}
</a>

{{- /* whitespace stripped here to avoid trailing newline in rendered result caused by file EOL */ -}}
```

## Transforming images

```go-html-template {title="layouts/_default/_markup/render-image.html"}
{{- $url := urls.Parse .Destination -}}
{{- $scheme := $url.Scheme -}}

<img src="
  {{- if eq $scheme "" -}}
    {{- if strings.HasSuffix $url.Path ".md" -}}
      {{- relref .Page .Destination | safeURL -}}
    {{- else -}}
      {{- printf "/%s%s" .Page.File.Dir .Destination | safeURL -}}
    {{- end -}}
  {{- else -}}
    {{- .Destination | safeURL -}}
  {{- end -}}"
  {{- with .Title }} title="{{ . | safeHTML }}"{{- end -}}
  {{- with .Text }} alt="{{ . | safeHTML }}"
  {{- end -}}
/>

{{- /* whitespace stripped here to avoid trailing newline in rendered result caused by file EOL */ -}}
```