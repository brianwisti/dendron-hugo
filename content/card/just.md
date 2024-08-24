---
created: '2024-02-10 14:44:30'
description: ''
fname: pub.card.just
id: c5u9lvkfykm0doxet1an64l
title: Just
updated: '2024-02-10 14:44:46'
---

> Just a command runner

# Loading from `.env`

Once you tell it where to look, `just` loads dotenv files and treats its contents as environment variables.

So if my `.env` looks like this:

```sh
VAULT_HOME="/home/random/vaults/v2024"
```

And my justfile has this:

```makefile
dotenv-file := ".env"

export:
  obsidian-export $VAULT_HOME site/content
```

Then I can stop hard-coding paths in my [obsidian-export]({{< relref "/card/obsidian-export.md" >}}) invocation.

# Related

- <https://github.com/casey/just>