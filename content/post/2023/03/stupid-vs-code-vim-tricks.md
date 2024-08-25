---
categories:
- note
created: '2024-02-10 17:26:33'
date: 2023-03-20 00:00:00+00:00
description: ''
fname: pub.post.2023.03.stupid-vs-code-vim-tricks
id: qsa8htpcpirjgtwfornfjo4
slug: stupid-vs-code-vim-tricks
syndication:
  linkedin: https://www.linkedin.com/posts/brianwisti_stupid-vs-code-vim-tricks-activity-7043773885921599488-qAYr
  mastodon: https://hackers.town/@randomgeek/110058842352483483
tags:
- vs-code
- config
title: Stupid Vs Code Vim Tricks
updated: '2024-08-25 18:24:23'
---

Still trying my experiment with using [Dendron]({{< relref "/card/dendron.md" >}}) in [Visual Studio Code]({{< relref "/card/vs-code.md" >}}) as part of some sort of public second brain. Honestly I don't know how long that'll last, so I figure better share the fun stuff I learn here too.

Anyways this afternoon I installed the [Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim) extension and learned just enough about custom key bindings to add a few.

```json{title="settings.json"}
{
  "vim.leader": "<space>",
  "vim.normalModeKeyBindings": [
    {
      "before": ["<leader>", "t", "l"],
      "commands": ["workbench.action.toggleSidebarVisibility"]
    },
    {
      "before": ["<leader>", "t", "r"],
      "commands": ["workbench.action.toggleAuxiliaryBar"]
    },
    {
      "before": ["<leader>", "t", "t"],
      "commands": ["workbench.action.toggleLightDarkThemes"]
    }
  ]
}
```

- `vim.leader` is handy as a prefix for extended custom bindings in Vim; I prefer the spacebar as my leader
- `<leader> t l` toggles my left sidebar
- `<leader> t r` toggles my right sidebar
- `<leader> t t` toggles between light and dark theme

These bindings look and work very similar to some [Logseq]({{< relref "/card/logseq.md" >}}) default bindings. That's no accident. I like those bindings.