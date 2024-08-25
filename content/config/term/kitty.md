---
created: '2024-02-10 05:07:31'
description: ''
fname: pub.config.term.kitty
id: tjirhkot7ic4chgsucmiwnp
title: Kitty
updated: '2024-02-10 05:08:14'
---

I don't use it as often as WezTerm these days, but it's still nice.
Just a few of the mildest variations from Kitty defaults.

```conf
//- file:kitty/kitty.conf

// ==> Use Fantasque Sans Mono.

// ==> Handle symbols.
```

## Fonts

```conf
//- Use Fantasque Sans Mono
font_family FantasqueSansMono Nerd Font
font_size 14
```

Trying some symbol font funkiness. Taking lots of hints from [erwin.co][erwin-co].

[erwin-co]: https://erwin.co/kitty-and-nerd-fonts/

```conf
//- Handle symbols
# "Nerd Fonts - Pomicons"
symbol_map  U+E000-U+E00D Symbols Nerd Font Mono

# "Nerd Fonts - Powerline"
symbol_map U+e0a0-U+e0a2,U+e0b0-U+e0b3 Symbols Nerd Font Mono

# "Nerd Fonts - Powerline Extra"
symbol_map U+e0a3-U+e0a3,U+e0b4-U+e0c8,U+e0cc-U+e0d2,U+e0d4-U+e0d4 Symbols Nerd Font Mono

# "Nerd Fonts - Symbols original"
symbol_map U+e5fa-U+e62b Symbols Nerd Font Mono

# "Nerd Fonts - Devicons"
symbol_map U+e700-U+e7c5 Symbols Nerd Font Mono

# "Nerd Fonts - Font awesome"
symbol_map U+f000-U+f2e0 Symbols Nerd Font Mono

# "Nerd Fonts - Font awesome extension"
symbol_map U+e200-U+e2a9 Symbols Nerd Font Mono

# "Nerd Fonts - Octicons"
symbol_map U+f400-U+f4a8,U+2665-U+2665,U+26A1-U+26A1,U+f27c-U+f27c Symbols Nerd Font Mono

# "Nerd Fonts - Font Linux"
symbol_map U+F300-U+F313 Symbols Nerd Font Mono

#  Nerd Fonts - Font Power Symbols"
symbol_map U+23fb-U+23fe,U+2b58-U+2b58 Symbols Nerd Font Mono

#  "Nerd Fonts - Material Design Icons"
symbol_map U+f500-U+fd46 Symbols Nerd Font Mono

# "Nerd Fonts - Weather Icons"
symbol_map U+e300-U+e3eb Symbols Nerd Font Mono

# Misc Code Point Fixes
symbol_map U+21B5,U+25B8,U+2605,U+2630,U+2632,U+2714,U+E0A3,U+E615,U+E62B Symbols Nerd Font Mono
```