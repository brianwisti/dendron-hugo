---
created: '2024-02-10 04:25:40'
description: ''
fname: pub.card.sdkman
id: p3hqo78bl3mzha5mhroytp8
title: Sdkman
updated: '2024-08-25 17:53:37'
---

Command-line tool for version management of [Java]({{< relref "/card/java.md" >}}) and related tools for UNIX-like systems and Windows+MinGW.

## Jots

Installing SDKMAN

```sh
curl -s "https://get.sdkman.io" | bash
```

Get help for a specific command

```sh
sdk help list
```

List available versions for a specific tool

```sh
sdk list java
```

Install a specific JDK:

```sh
sdk install java 17.0.8-tem
```

Install a particular JVM tool:

```sh
sdk install maven
```

## Related

- [Home - SDKMAN! the Software Development Kit Manager](https://sdkman.io/)