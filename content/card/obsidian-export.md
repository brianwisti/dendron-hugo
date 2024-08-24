---
created: '2024-02-10 04:38:27'
description: ''
fname: pub.card.obsidian-export
id: tnidqxfl20a237ww8fujax6
title: obsidian-export
updated: '2024-02-10 04:40:00'
---

A [Rust]({{< relref "/card/rust.md" >}}) library and CLI tool for exporting [Obsidian]({{< relref "/card/obsidian.md" >}}) vault contents into regular [Markdown]({{< relref "/card/markdown.md" >}}). This cuts down a few steps for your [Static Site Generator]({{< relref "/card/static-site-generator.md" >}}) or other processing scripts.

There's curl-bash installation instructions corresponding to specific versions on the [Releases](https://github.com/zoni/obsidian-export/releases) page.

The `obsidian-export` README provides sample templates for [Using Obsidian Export with Hugo]({{< relref "/card/using-obsidian-export-with-hugo.md" >}})

# Jots

Obsidian Sync doesn't copy dotfiles. `.export-ignore` needs to be added on every platform that you're running `obsidian-export`. So, better keep track of *inbox.my-export-ignore*.

Transforms unavailable links – say, *2024-01-21 Sun* for example – into unlinked italicized text during export.

# Related

- [GitHub - zoni/obsidian-export: Rust library and CLI to export an Obsidian vault to regular Markdown](https://github.com/zoni/obsidian-export)