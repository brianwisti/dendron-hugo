---
created: '2024-02-10 05:20:30'
description: ''
fname: pub.config.linux.systemd
id: sozri2miptv2vmonythx458
title: Systemd
updated: '2024-02-10 05:20:40'
---

The `autostart` target describes services that should start with a fresh user session. Or it will eventually. Mostly I'm just working on a reproducible setup for [dex][dex].

[dex]: https://github.com/jceb/dex

```conf
//- file:systemd/user/autostart.target
Description=current graphical user session
RefuseManualStart=no
StopWhenUnneeded=no
```