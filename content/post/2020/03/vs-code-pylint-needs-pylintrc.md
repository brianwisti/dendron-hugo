---
created: '2024-02-13 17:22:12'
date: 2020-03-19
description: ''
fname: pub.post.2020.03.vs-code-pylint-needs-pylintrc
id: fcq5sr416wxgi3ovb9lg6b6
title: VS Code Pylint Needs Pylintrc
updated: '2024-08-07 19:01:02'
---

[Visual Studio Code]({{< relref "/card/vs-code.md" >}}) doesn’t seem to pick up my environment’s [PYTHONPATH](https://docs.python.org/3.8/using/cmdline.html#envvar-PYTHONPATH) when running [pylint](https://www.pylint.org/). Makes project-local modules a headache. The solution: put it in `${workspaceFolder}/.pylintrc`:

```ini
[MASTER]
init-hook='import sys; sys.path.append("pylib")'
```

Okay, I got more planned for today than messing with code. Back to that other stuff.