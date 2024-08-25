---
created: '2024-02-10 05:15:22'
description: ''
fname: pub.config.shell.nushell
id: 06cijzannoyzg7m95lqilyb
title: Nushell
updated: '2024-02-10 05:18:20'
---

[Nushell][nushell] may still be in development, but it's getting pretty darn useful.

[nushell]: https://nushell.sh

## `config.nu`

Been taking a closer look at the [default config](https://github.com/nushell/nushell/blob/main/crates/nu-utils/src/sample_config/default_config.nu), mainly so I can understand what I want to change.

```nushell
// ==> Define completions module.

use completions *

// ==> Define my themes.
// ==> Declare my config.
```

### Completions

The completions come directly from the default.

```nu
//- Define completions module
module completions {
  # Custom completions for external commands (those outside of Nushell)
  # Each completions has two parts: the form of the external command, including its flags and parameters
  # and a helper command that knows how to complete values for those flags and parameters
  #
  # This is a simplified version of completions for git branches and git remotes
  def "nu-complete git branches" [] {
    ^git branch | lines | each { |line| $line | str replace '[\*\+] ' '' | str trim }
  }

  def "nu-complete git remotes" [] {
    ^git remote | lines | each { |line| $line | str trim }
  }

  export extern "git checkout" [
    branch?: string@"nu-complete git branches" # name of the branch to checkout
    -b: string                                 # create and checkout a new branch
    -B: string                                 # create/reset and checkout a branch
    -l                                         # create reflog for new branch
    --guess                                    # second guess 'git checkout <no-such-branch>' (default)
    --overlay                                  # use overlay mode (default)
    --quiet(-q)                                # suppress progress reporting
    --recurse-submodules: string               # control recursive updating of submodules
    --progress                                 # force progress reporting
    --merge(-m)                                # perform a 3-way merge with the new branch
    --conflict: string                         # conflict style (merge or diff3)
    --detach(-d)                               # detach HEAD at named commit
    --track(-t)                                # set upstream info for new branch
    --force(-f)                                # force checkout (throw away local modifications)
    --orphan: string                           # new unparented branch
    --overwrite-ignore                         # update ignored files (default)
    --ignore-other-worktrees                   # do not check if another worktree is holding the given ref
    --ours(-2)                                 # checkout our version for unmerged files
    --theirs(-3)                               # checkout their version for unmerged files
    --patch(-p)                                # select hunks interactively
    --ignore-skip-worktree-bits                # do not limit pathspecs to sparse entries only
    --pathspec-from-file: string               # read pathspec from file
  ]

  export extern "git push" [
    remote?: string@"nu-complete git remotes", # the name of the remote
    refspec?: string@"nu-complete git branches"# the branch / refspec
    --verbose(-v)                              # be more verbose
    --quiet(-q)                                # be more quiet
    --repo: string                             # repository
    --all                                      # push all refs
    --mirror                                   # mirror all refs
    --delete(-d)                               # delete refs
    --tags                                     # push tags (can't be used with --all or --mirror)
    --dry-run(-n)                              # dry run
    --porcelain                                # machine-readable output
    --force(-f)                                # force updates
    --force-with-lease: string                 # require old value of ref to be at this value
    --recurse-submodules: string               # control recursive pushing of submodules
    --thin                                     # use thin pack
    --receive-pack: string                     # receive pack program
    --exec: string                             # receive pack program
    --set-upstream(-u)                         # set upstream for git pull/status
    --progress                                 # force progress reporting
    --prune                                    # prune locally removed refs
    --no-verify                                # bypass pre-push hook
    --follow-tags                              # push missing but relevant tags
    --signed: string                           # GPG sign the push
    --atomic                                   # request atomic transaction on remote side
    --push-option(-o): string                  # option to transmit
    --ipv4(-4)                                 # use IPv4 addresses only
    --ipv6(-6)                                 # use IPv6 addresses only
  ]
}

```

### Theme

Again, straight from the defaults.
For more on themes see the Nushell book section on [coloring and theming][nu-theming].

[nu-theming]: https://www.nushell.sh/book/coloring_and_theming.html

```nu
//- Define my themes
let default_theme = {
    # color for nushell primitives
    separator: white
    leading_trailing_space_bg: { attr: n } # no fg, no bg, attr none effectively turns this off
    header: green_bold
    empty: blue
    bool: white
    int: white
    filesize: white
    duration: white
    date: white
    range: white
    float: white
    string: white
    nothing: white
    binary: white
    cellpath: white
    row_index: green_bold
    record: white
    list: white
    block: white
    hints: dark_gray

    # shapes are used to change the cli syntax highlighting
    shape_garbage: { fg: "#FFFFFF" bg: "#FF0000" attr: b}
    shape_binary: purple_bold
    shape_bool: light_cyan
    shape_int: purple_bold
    shape_float: purple_bold
    shape_range: yellow_bold
    shape_internalcall: cyan_bold
    shape_external: cyan
    shape_externalarg: green_bold
    shape_literal: blue
    shape_operator: yellow
    shape_signature: green_bold
    shape_string: green
    shape_string_interpolation: cyan_bold
    shape_datetime: cyan_bold
    shape_list: cyan_bold
    shape_table: blue_bold
    shape_record: cyan_bold
    shape_block: blue_bold
    shape_filepath: cyan
    shape_globpattern: cyan_bold
    shape_variable: purple
    shape_flag: blue_bold
    shape_custom: green
    shape_nothing: light_cyan
}
```

### The config record

Here's the important part.
Got a few little variations from the default but there's a heck of a lot unchanged.

```nu
//- Declare my config

let-env config = {
  color_config: $default_theme
  edit_mode: emacs # emacs, vi
  float_precision: 2
  footer_mode: "25" # always, never, number_of_rows, auto
  use_ansi_coloring: true
  use_grid_icons: true

  filesize: {
    # true: KB, GB, etc
    # false: KiB, GiB, etc
    # On WSL, I get KiB if I don't explicitly set true
    metric: true
  }

  menus: [
      # Configuration for default nushell menus
      # Note the lack of souce parameter
      {
        name: completion_menu
        only_buffer_difference: false
        marker: "| "
        type: {
            layout: columnar
            columns: 4
            col_width: 20   # Optional value. If missing all the screen width is used to calculate column width
            col_padding: 2
        }
        style: {
            text: green
            selected_text: green_reverse
            description_text: yellow
        }
      }
      {
        name: history_menu
        only_buffer_difference: true
        marker: "? "
        type: {
            layout: list
            page_size: 10
        }
        style: {
            text: green
            selected_text: green_reverse
            description_text: yellow
        }
      }
      {
        name: help_menu
        only_buffer_difference: true
        marker: "? "
        type: {
            layout: description
            columns: 4
            col_width: 20   # Optional value. If missing all the screen width is used to calculate column width
            col_padding: 2
            selection_rows: 4
            description_rows: 10
        }
        style: {
            text: green
            selected_text: green_reverse
            description_text: yellow
        }
      }
      # Example of extra menus created using a nushell source
      # Use the source field to create a list of records that populates
      # the menu
      {
        name: commands_menu
        only_buffer_difference: false
        marker: "# "
        type: {
            layout: columnar
            columns: 4
            col_width: 20
            col_padding: 2
        }
        style: {
            text: green
            selected_text: green_reverse
            description_text: yellow
        }
        source: { |buffer, position|
            $nu.scope.commands
            | where command =~ $buffer
            | each { |it| {value: $it.command description: $it.usage} }
        }
      }
      {
        name: vars_menu
        only_buffer_difference: true
        marker: "# "
        type: {
            layout: list
            page_size: 10
        }
        style: {
            text: green
            selected_text: green_reverse
            description_text: yellow
        }
        source: { |buffer, position|
            $nu.scope.vars
            | where name =~ $buffer
            | sort-by name
            | each { |it| {value: $it.name description: $it.type} }
        }
      }
      {
        name: commands_with_description
        only_buffer_difference: true
        marker: "# "
        type: {
            layout: description
            columns: 4
            col_width: 20
            col_padding: 2
            selection_rows: 4
            description_rows: 10
        }
        style: {
            text: green
            selected_text: green_reverse
            description_text: yellow
        }
        source: { |buffer, position|
            $nu.scope.commands
            | where command =~ $buffer
            | each { |it| {value: $it.command description: $it.usage} }
        }
      }
  ]
  keybindings: [
    {
      name: completion_menu
      modifier: none
      keycode: tab
      mode: emacs # Options: emacs vi_normal vi_insert
      event: {
        until: [
          { send: menu name: completion_menu }
          { send: menunext }
        ]
      }
    }
    {
      name: completion_previous
      modifier: shift
      keycode: backtab
      mode: [emacs, vi_normal, vi_insert] # Note: You can add the same keybinding to all modes by using a list
      event: { send: menuprevious }
    }
    {
      name: history_menu
      modifier: control
      keycode: char_x
      mode: emacs
      event: {
        until: [
          { send: menu name: history_menu }
          { send: menupagenext }
        ]
      }
    }
    {
      name: history_previous
      modifier: control
      keycode: char_z
      mode: emacs
      event: {
        until: [
          { send: menupageprevious }
          { edit: undo }
        ]
      }
    }
    # Keybindings used to trigger the user defined menus
    {
      name: commands_menu
      modifier: control
      keycode: char_t
      mode: [emacs, vi_normal, vi_insert]
      event: { send: menu name: commands_menu }
    }
    {
      name: vars_menu
      modifier: control
      keycode: char_y
      mode: [emacs, vi_normal, vi_insert]
      event: { send: menu name: vars_menu }
    }
    {
      name: commands_with_description
      modifier: control
      keycode: char_u
      mode: [emacs, vi_normal, vi_insert]
      event: { send: menu name: commands_with_description }
    }
  ]
}
```

## `env.nu`

### Set up my prompt

Adds a Starship prompt on the right and a timestamp on the left.

```nu
def create_left_prompt [] {
  starship prompt --cmd-duration $env.CMD_DURATION_MS $'--status=($env.LAST_EXIT_CODE)'
}
def create_right_prompt [] {
    let time_segment = ([
        (date now | date format '%m/%d/%Y %r')
    ] | str collect)

    $time_segment
}
let-env STARSHIP_SHELL = "nu"
let-env PROMPT_COMMAND = { create_left_prompt }
let-env PROMPT_COMMAND_RIGHT = { create_right_prompt }
let-env PROMPT_INDICATOR = { "" }
let-env PROMPT_INDICATOR_VI_INSERT = { ": " }
let-env PROMPT_INDICATOR_VI_NORMAL = { "〉" }
let-env PROMPT_MULTILINE_INDICATOR = { "::: " }
```

### Environment conversions

Nushell isn't my login shell yet.
This logic converts existing environment variables to Nu equivalents.
So far it works on Linux, Windows, and macOS.

```nu
let-env ENV_CONVERSIONS = {
  "PATH": {
    from_string: { |s| $s | split row (char esep) }
    to_string: { |v| $v | str collect (char esep) }
  }
  "Path": {
    from_string: { |s| $s | split row (char esep) }
    to_string: { |v| $v | str collect (char esep) }
  }
}
```

### Nu libraries and plugins

I don't have many yet, but here's where Nu should expect to find them.

```nu
let-env NU_LIB_DIRS = [
    ($nu.config-path | path dirname | path join 'scripts')
]
let-env NU_PLUGIN_DIRS = [
    ($nu.config-path | path dirname | path join 'plugins')
]
```

### Path management

Environment variables in Nushell are a bit more strict than other shells.
You can't just re-export.
You have to redeclare.
So this function helps me with my most common case:
managing entries in the executable path.

If `new_path` isn't already in `$env.PATH`,
a new `$env.PATH` is declared by prepending the new path to the current list of paths.

```nu
def-env ensure-path [new_path: string] {
  let full_path = ($new_path | path expand)
  let updated_env_path = (
    if $new_path in $env.PATH { $env.PATH }
    else {
      $env.PATH | prepend $full_path
    }
  )
  let-env PATH = $updated_env_path
}
```

And then I use it for the paths I care about most.
Mostly useful when using Nushell as login,
since these entries are usually picked up from the parent shell.

```nu
(ensure-path "~/.local/bin")
(ensure-path "~/.volta/bin")
(ensure-path "~/.cargo/bin")
(ensure-path "~/.rakubrew/bin")
```

Kinda suggests maybe these invocations should go in `login.nu`.

### Miscellaneous

Load the script that nicely formats Taskwarrior output.

```nu
source /home/random/.config/nushell/lib/task.nu
```

Add a function to read from EDN sources such as output by `nbb-logseq`.
Requires the `jet` CLI tool.

```nu
def from-edn [] {
  $in | str collect | jet --to json | from json
}
```

## `login.nu`

For my occasional experiments using Nu as my login shell.
Evaluated *after* `env.nu` and `config.nu`.

```nushell
let-env BAT_THEME = 'Solarized (dark)'
let-env BF = '$albumartist | $album | $track/$tracktotal | $title'
let-env CLICOLOR = '1'
let-env EDITOR = 'nvim'
let-env LANG = 'en_US.UTF-8'
let-env NNN_FALLBACK_OPENER = 'xdg-open'
let-env PAGER = 'less -FRX'
let-env PLENV_HOME = '/home/random/.plenv'
let-env PYENV_ROOT = '/home/random/.pyenv'
let-env PYENV_SHELL = 'nu'
let-env PYENV_VIRTUALENV_INIT = '1'
let-env RAKUBREW_HOME = '~/.rakubrew'
let-env STARSHIP_SHELL = 'nu'
let-env TERM = 'xterm-256color'
```

## `lib/task.nu`

## `task.nu`

The idea here is to make a pretty Nu-style table from my Taskwarrior reports.

```nushell
//- file:nushell/lib/task.nu
# Prettify taskwarrior output with nushell

# Ensure field has string value or explicit null
def upsert-string [field] {
  $in | upsert $field { |it|
    let value = ($in | get -i $field)

    if ($value | empty?) { "" } else { $value | str collect " " }
  }
}

# Ensure field has datetime value or explicit null
def upsert-date [field] {
  $in | upsert $field { |it|
    let value = ($in | get -i $field)

    if ($value | empty?) { $nothing } else { $value | into datetime }
  }
}

# Format a taskwarrior export into a table
def from-tw [] {
  (
    $in
    | from json
    | upsert-string project
    | upsert-date entry
    | upsert-date modified
    | upsert-date end
  )
}

# stock reports

# next (the default)
def tw-next [] {
  (
    task status:pending -WAITING limit:page -Work -pay -finances -personal export
    | from-tw
    | upsert-string tags
    | select id entry priority project tags description urgency
    | sort-by -r urgency
    | rename ID Age P Project Tag Description Urg
  )
}


# active
# all
# blocked
# blocking
# burndown.daily
# burndown.monthly
# burndown.weekly
# completed
# ghistory.annual
# ghistory.monthly
# history.annual
# history.monthly
# information
# list
# long
# ls
# minimal
# newest
# oldest
# overdue
# projects
# ready
# recurring
# summary
# tags
# unblocked
# waiting
```