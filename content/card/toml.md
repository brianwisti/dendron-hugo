---
created: '2024-02-10 16:16:31'
description: ''
fname: pub.card.toml
id: ejdmzat04vs74y9rmsg7fey
title: TOML
updated: '2024-02-10 16:16:41'
---

Tom's Obvious Minimal Language

A minimal configuration file format.

## Syntax

### Comments

```toml
# comments are single-line
```

### Pairs

```toml
name = value
```

#### Keys

- bare: `name`
- quoted: `"user name"` or `'user name'`
- dotted: `user.name` or `'my."user name"'` but please no

#### Value Types

- string
- integer
- float
- boolean
- offset date-time
- local date-time
- local time
- array
- table

## Related

- <https://toml.io/en/>
- <https://github.com/toml-lang/toml>
- [TOML: English v1.0.0](https://toml.io/en/v1.0.0)