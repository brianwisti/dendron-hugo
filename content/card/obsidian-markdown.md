---
created: '2024-02-10 14:21:23'
description: ''
fname: pub.card.obsidian-markdown
id: kzins5n04bkkraq5b6yjj70
title: Obsidian Markdown
updated: '2024-08-25 17:55:34'
---

Special considerations and features that I care about for [Markdown]({{< relref "/card/markdown.md" >}}) in [Obsidian]({{< relref "/card/obsidian.md" >}})

<!--more-->

## Linking

- Internal links with `[[link]]`
- Internal images with regular `![](link)` or `![[link]]`
- YouTube embeds with `![](link)`

## Callouts

aka admonitions

```md
> [!TYPE] OPTIONAL TITLE
> BODY
```

Officially supported types. Each entry gets its own rendering style. Any unrecognized type is treated as *Note*.

- Note
- Abstract / summary / tldr
- Info
- Todo
- Tip / Hint / Important
- Success / Check / Done
- Question / Help / Faq
- Warning / Caution / Attention
- Failure / Fail / Missing
- Danger / Error
- Bug
- Example
- Quote / Cite

## Related

- <https://help.obsidian.md/Editing+and+formatting/Obsidian+Flavored+Markdown>