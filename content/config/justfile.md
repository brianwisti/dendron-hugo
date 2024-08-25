---
created: '2024-02-10 05:05:16'
description: ''
fname: pub.config.justfile
id: ooau487gm58qfty9d0vdatx
title: Justfile
updated: '2024-02-10 05:05:34'
---

Using [Yarner]({{< relref "/card/yarner.md" >}}) to tangle the file that drives the whole process? I should be ashamed of myself. I'm not, but I feel like I should be.

## Building everything with Yarner

I let Yarner do its thing. Then I copy my newly generated `justfile` and dotbot configs to the project root, making sure to back up the current copies. If I screw up, I can always go to the backup. If I screw up bad, I can always go back to Git history. If I screw up *real* bad, I have another computer.

```justfile
build:
  yarner
  cp -b code/justfile ./
  cp -b code/install.conf.yaml ./
```

## Installing my configs with dotbot

Invoke dotbot to link with files and directories.

```justfile
install:
  ./install -v
```

## Cleaning

Remove the build artifacts if they exist. Better be careful about running this, as it *will* confuse Dotbot.

```justfile
clean:
  [ -d code ] && rm -r code
  [ -d docs ] && rm -r docs
```

## Checking window managers

It's a manual process: run a nested X server with `awesome` or `qtile`.
If anything is off, fix it and reload from inside the nested server.

```justfile
awesome:
  Xephyr :5 & sleep 1 ; DISPLAY=:5 awesome

qtile:
  Xephyr :5 & sleep 1 ; DISPLAY=:5 qtile start
```

## Anything else?

I need some kind of test process, but better think about what that would look like before I try.