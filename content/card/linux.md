---
created: '2024-02-10 04:29:33'
description: ''
fname: pub.card.linux
id: 0ladvc25wb2jsm3sx460jjm
title: Linux
updated: '2024-08-25 17:18:13'
---

One of the more widespread open source operating systems

<!--more-->

## `timedatectl`

Control system for time and date details on Linux

Recurring issue on my frequent Linux reinstalls: reboot into [Windows]({{< relref "/card/windows.md" >}}), and the time is off by my local UTC offset. Fix that in Linux by telling the system that the *Real Time Clock (RTC)* uses local time

```sh
timedatectl set-local-rtc 1 --adjust-system-clock
```

## Related

- [Linux.org](https://linux.org)