---
created: '2024-02-10 14:26:40'
description: ''
fname: pub.card.vs-code-snippets
id: 22ieo2f8lk6zolzxu5zc1mn
title: VS Code Snippets
updated: '2024-02-10 14:27:05'
---

Micro-templates for [Visual Studio Code]({{< relref "/card/vs-code.md" >}}) basically

# How

Manage snippets with *Snippets: Configure User Snippets*

Launch snippet selector with `C-SPC`

# Snippet Variables

The breakdown they use does keep the list from getting overwhelming. So I'll just sing along.

## Buffer, workspace, and clipboard variables

| Variable            | Value                                       |
| ------------------- | ------------------------------------------- |
| `TM_SELECTED_TEXT`  | currently selected text if any              |
| `TM_CURRENT_LINE`   | current line's contents                     |
| `TM_CURRENT_WORD`   | word under cursor if any                    |
| `TM_LINE_INDEX`     | line number (zero-indexed)                  |
| `TM_LINE_NUMBER`    | line number (one-indexed)                   |
| `TM_FILENAME`       | current document filename                    |
| `TM_FILENAME_BASE`  | current document filename w/o extension      |
| `TM_DIRECTORY`      | current document directory                  |
| `TM_FILEPATH`       | current document absolute path              |
| `RELATIVE_FILEPATH` | current document path relative to workspace |
| `CLIPBOARD`         | primary clipboard contents                  |
| `WORKSPACE_NAME`    | current workspace name                      |
| `WORKSPACE_FOLDER`  | current workspace / folder absolute path    |
| `CURSOR_INDEX`      | cursor number (zero-indexed)                |
| `CURSOR_NUMBER`     | cursor number (one-indexed)                 |

## Date and time variables

| Variable                   | Value                          |
| -------------------------- | ------------------------------ |
| `CURRENT_YEAR`             | year as `YYYY...`              |
| `CURRENT_YEAR_SHORT`       | year as `YY`                   |
| `CURRENT_MONTH`            | month as `MM`                  |
| `CURRENT_MONTH_NAME`       | full month name                |
| `CURRENT_MONTH_NAME_SHORT` | short month name               |
| `CURRENT_DATE`             | day of the month as `DD`       |
| `CURRENT_DAY_NAME`         | full name for day of the week  |
| `CURRENT_DAY_NAME_SHORT`   | short name for day of the week |
| `CURRENT_HOUR`             | current hour as `HH` (24 hour) |
| `CURRENT_MINUTE`           | current minute as `MM`         |
| `CURRENT_SECOND`           | current second as `SS`         |
| `CURRENT_SECONDS_UNIX`     | seconds since the Unix epoch   |

## Random value generation variables

| Variable     | Value                   |
| ------------ | ----------------------- |
| `RANDOM`     | 6 random decimal digits |
| `RANDOM_HEX` | 6 random hex digits     |
| `UUID`       | version 4 UUID          |

## Language-appropriate comment generation variables

| Variable              | Value                                   |
| --------------------- | --------------------------------------- |
| `BLOCK_COMMENT_START` | block comment start for buffer language |
| `BLOCK_COMMENT_END`   | block comment end for buffer language   |
| `LINE_COMMENT`        | line comment start for buffer language  |

# Related

- [Snippets in Visual Studio Code](https://code.visualstudio.com/docs/editor/userdefinedsnippets)