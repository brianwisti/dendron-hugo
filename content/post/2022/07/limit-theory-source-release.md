---
created: '2024-02-11 18:09:36'
date: '2022-07-24T00:00:00.000Z'
description: ''
fname: pub.post.2022.07.limit-theory-source-release
id: k224nw183d0et1nbxpldmxc
slug: limit-theory-source-release
tags:
- gaming
- limit-theory
- lua
title: Limit Theory Source Release
updated: '2024-02-11 18:10:37'
---

Josh Parnell released the source code for [Limit Theory](http://ltheory.com), one of those Kickstarter-backed game projects that kind of imploded on a combo of complexity and high expectations.

<!--more-->

[Limit Theory Update 54: Source Code Release](https://www.kickstarter.com/projects/joshparnell/limit-theory-an-infinite-procedural-space-game/posts/3564318)

> At long last, it's time for the source code release that I promised years ago. Today I'll be releasing four open-source repositories on GitHub, representing three different times in LT's development history.

The repos:

[Limit Theory Protoype](https://github.com/JoshParnell/ltprototype)
: a binary installer of the initial demo for Windows

[Limit Theory Old](https://github.com/JoshParnell/ltheory-old)
: phase 1 of the project, written 2012-2015 in C++ with a custom scripting language
: "While this code is dated compared to the newer C/Lua LT, it is arguably meatier in gameplay implementation."

[LibPHX](https://github.com/JoshParnell/libphx)
: A game engine focusing on core 3D game support, with you writing your actual game in [Lua](https://lualang.org)
: "The engine's C interface, combined with LuaJIT's FFI technology, allows for scripts to make zero-overhead calls into the engine, thus allowing *the majority* of game logic and control to remain in script."

[Limit Theory](https://github.com/JoshParnell/ltheory)
: The 2015-2018 game code, written in Lua to hook into LibPHX

All released under the [Unlicense](https://unlicense.org) — an explicitly public domain license.

Over 5,000 people pledged nearly $188,000 total. I put in $75. Parnell took the Kickstarter success personally, worked his butt off, couldn't get the game where he wanted it, and burned out bad. Big Ambitious Space Games have a lot of fiddly bits, no matter how many developers or how much money you have. Just ask [Frontier](https://www.elitedangerous.com), [Hello](https://www.nomanssky.com), and [Chris Roberts](https://robertsspaceindustries.com/star-citizen/).

I feel bad for him — Parnell, not Roberts — and I'm grateful he released the  source code. I hope he gets some kind of closure from this. He deserves it.

Now if you'll excuse me, I'm gonna go learn some more [Lua]({{< relref "/card/lua.md" >}}).