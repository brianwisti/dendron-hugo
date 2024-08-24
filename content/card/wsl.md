---
created: '2024-02-10 16:19:11'
description: ''
fname: pub.card.wsl
id: khp89xymcj1u2fb9bldzob8
title: WSL
updated: '2024-02-10 16:20:39'
---

Windows Subsystem for Linux

Either a heavyweight container or a lightweight VM. Either way, it's how I do *inbox.linux* when on *inbox.windows*.

# CLI Usage

```plaintext
wsl [ARGUMENT] [OPTIONS...] [COMMAND]
```

Launches _default shell_ if `COMMAND` is not specified and `ARGUMENT` is not
provided.

## `--help`

Show usage information

## Launching shells

probably should be a sub-item of _executing commands_

`wsl ~`

Launch default distribution and start user session in distro-user's `$HOME`

## WSL Management commands

### `--install`

With no additional arguments, installs WSL and Microsoft's default preference distro (Ubuntu)

### `--list`

Show installed WSL distributions

```plaintext
〉wsl --list
Windows Subsystem for Linux Distributions:
Ubuntu (Default)
docker-desktop-data
Ubuntu-22.04
NixOS
docker-desktop
```

#### `--list --verbose`

Add WSL version and current status to WSL distribution list

```plaintext
〉wsl --list --verbose
  NAME                   STATE           VERSION
* Ubuntu                 Running         2
  docker-desktop-data    Running         2
  Ubuntu-22.04           Stopped         2
  NixOS                  Stopped         2
  docker-desktop         Running         2
```

#### `--list --online`

Show distributions available to install on WSL

```plaintext
> wsl --list --online
The following is a list of valid distributions that can be installed.
Install using 'wsl.exe --install <Distro>'.

NAME               FRIENDLY NAME
Ubuntu             Ubuntu
Debian             Debian GNU/Linux
kali-linux         Kali Linux Rolling
SLES-12            SUSE Linux Enterprise Server v12
SLES-15            SUSE Linux Enterprise Server v15
Ubuntu-18.04       Ubuntu 18.04 LTS
Ubuntu-20.04       Ubuntu 20.04 LTS
OracleLinux_8_5    Oracle Linux 8.5
OracleLinux_7_9    Oracle Linux 7.9
```

### `--set-default DISTRIBUTION`

Record a new preference for default Linux distribution.

### `--shutdown`

Terminate all running distributions and the WSL manager

> [!WARNING]
> Docker will complain.

### `--terminate DISTRIBUTION`

Terminates specified distribution while leaving other distros and WSL manager
alone.

```plaintext
〉wsl --terminate Ubuntu
The operation completed successfully.
```

Docker will complain if you terminate a distribution it has been integrated with.

### `--unregister DISTRIBUTION`

Remove named distribution from WSL registry so it can be reinstalled or cleaned up.

```plaintext
〉wsl --unregister NixOS
Unregistering.
The operation completed successfully.
```

## Related

- <https://docs.microsoft.com/en-us/windows/wsl/>
- [Run Linux GUI apps on the Windows Subsystem for Linux](https://docs.microsoft.com/windows/wsl/tutorials/gui-apps)
- [Diagnosing "cannot open display" type issues with WSLg](https://github.com/microsoft/wslg/wiki/Diagnosing-%22cannot-open-display%22-type-issues-with-WSLg)