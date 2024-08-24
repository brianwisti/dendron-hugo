---
created: '2024-02-18 05:19:15'
date: 2007-12-29 00:00:00+00:00
description: ''
fname: pub.post.2007.12.dv9310-bios-issues
id: 8xjk166opu5yi24vbk77u06
redirects:
- /blogspot/2007/12/29_now-that-both-of-my-machines-are.html
- /post/2007/now-that-both-of-my-machines-are/
- /2007/12/29/dv9310-bios-issues/
slug: dv9310-bios-issues
tags:
- i-fixed-it
- blogspot
title: Dv9310 BIOS Issues
updated: '2024-02-18 05:20:01'
---

I turned an offhand comment about how I fixed my problem into more of a step-by-step guide, in case some poor soul is in the same spot and finds me via Google.

Now that both of my machines are healing again - did I mention that a BIOS update flattened my HP dv9310? Oh, it flattened my HP all right. The new one effectively  makes the computer forget that it has a video card. If you do an update and the machine starts spontaneously rebooting, try this:

1. Boot into Safe Mode
2. Go to your Device Manager and disable the NVidia card. It's okay, you'll still have normal VGA.
3. Reboot in normal mode.
4. Go to the HP support site and download an older BIOS version.
5. Install that older BIOS.
6. Reboot.
7. Go to your Device Manager and re-enable the NVidia card.

Everything should be okay now.

Anyways, the machines are reconfigured, I've sparked my brain with a little Python code, and now I can get back to a Perl project that's been waiting over a month.