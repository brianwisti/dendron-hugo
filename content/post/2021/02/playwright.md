---
aliases:
- /bookmark/2021/02/playwright-dev/
created: '2024-02-11 19:52:53'
date: 2021-02-28 00:00:00+00:00
description: Cross-browser end-to-end testing for modern web apps
fname: pub.post.2021.02.playwright
id: j8y1s35gv7ejzq9m7gsqmze
slug: playwright-dev
tags:
- python
- testing
- browser-testing
title: Playwright for Python
updated: '2024-08-07 19:03:46'
---

There's a [Python]({{< relref "/card/python.md" >}}) interface to the very handy [Playwright](https://playwright.dev) browser automation library. The 1.9.x releases feel more Pythonic. Naming conventions, stuff like that. Feels much less like just a wrapper.

Don't forget to install browser drivers whenever you install or upgrade Playwright!

```bash
python -m playwright install
```

## With pytest

The [pytest-playwright](https://github.com/microsoft/playwright-pytest) plugin provides fixtures, marks, and extra `pytest` args for browser testing. So far the only fixture I've used is `page`, the stand-in for a default browser session. Pairs nicely with [pytest-django](https://pytest-django.readthedocs.io/)'s `live_server` fixture.

Headless by default, but use `pytest --headful` if you want to watch the browser do its thing.

> [!WARNING]
> Since pytest-playwright is still in *early* days — 0.0.12 as of this bookmark date — dependency managers might not acknowledge new releases. Watch the repo and manually update your dependencies when you see a new release.