---
created: '2024-02-10 05:10:31'
description: ''
fname: pub.config.shell.tmux
id: 6ftknhoq66ypubrsf8xa0tc
title: Tmu
updated: '2024-02-10 05:10:37'
---

Got it happy a while ago and haven't messed with it much since.

```conf
//- file:tmux.conf

// ==> Define terminal settings.
// ==> Handle the clipboard.
// ==> Manage display.
// ==> Define keybindings.
// ==> Configure the status bar.
// ==> Set theme colors.
```

## Figuring out terminal support

Always a bit of struggle with me for some reason.

```conf
//- Define terminal settings
# The terminal supports true color
set-option -g default-terminal "tmux-256color"
set-option -sa terminal-overrides ",*:RGB"
set-option -sa terminal-overrides ",xterm*:RGB"
```

## Clipboard and system integration

```conf
//- Handle the clipboard
# See /opt/local/share/doc/tmux-pasteboard/Usage.md
#if-shell 'test "$(uname -s)" = Darwin' 'set-option -g default-command "exec reattach-to-user-namespace -l zsh"'
set -s escape-time 1
set -g mouse on

if-shell "uname | grep -q Darwin" {
  bind-key -T copy-mode-vi 'y' \
    send -X copy-pipe-and-cancel 'reattach-to-user-namespace pbcopy'
  bind-key -T copy-mode-vi Enter \
    send -X copy-pipe-and-cancel 'reattach-to-user-namespace pbcopy'
} {
  bind-key -T copy-mode-vi 'y' \
    send -X copy-pipe-and-cancel 'xclip -in -selection clipboard'
  bind-key -T copy-mode-vi Enter \
    send -X copy-pipe-and-cancel 'xclip -in -selection clipboard'
}

set-option -g focus-events on
```

## Display

```conf
//- Manage display
# via https://github.com/gpakosz/.tmux/blob/master/.tmux.conf
set -g base-index 1          # window numbering
setw -g pane-base-index 1    # pane numbering
set -g renumber-windows on   # renumber when a window closed?
setw -g automatic-rename on # rename window to reflect current program?
set -g set-titles on         # set terminal title

set -g monitor-activity on
set -g visual-activity on
```

## Key bindings

```conf
//- Define keybindings
set-window-option -g xterm-keys on
set-window-option -g mode-keys vi

bind c new-window -c "#{pane_current_path}"
bind C new-window -- nu
bind r source-file ~/.tmux.conf \; display "Reloaded!"

bind \\ split-window -h -c "#{pane_current_path}"
unbind %

bind - split-window -v -c "#{pane_current_path}"
unbind '"'

bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
```

## Status bar

And its widgets.

```conf
//- Configure the status bar
set -g status on
set -g status-interval 10    # redraw status line after n seconds
set-window-option -g status-position top

# See also: https://github.com/samoshkin/tmux-config/blob/master/tmux/tmux.conf
wg_date="#[$color_secondary]%Y-%m-%d %H:%M%z#[default]"
#set -g status-right "#{prefix-highlight} #(task-counts) $wg_date"
set -g status-right "#{prefix-highlight} $wg_date"
```

## Colors

Sort of a Fairyfloss / SpaceDuck-friendly color scheme.

```conf
//- Set theme colors

// ==> Set default bar color.
// ==> Set active pane color.
// ==> Set inactive pane color.
// ==> Set active window color.
// ==> Set message color.
// ==> Set color when commands are run.
```

### Default bar color

```conf
//- Set default bar color
set-option -g status-style "bg=#1b1c36, fg=#ecf0c1"
```

### Active pane

```conf
//- Set active pane color
set -g pane-active-border-style "fg=#fccc96"
```

### Inactive pane

```conf
//- Set inactive pane color
set -g pane-border-style "fg=#686f9a"
```

### Active window

```conf
//- Set active window color
set-option -g window-status-current-style "bg=#686f9a, fg=#ffffff"
```

### Message

```conf
//- Set message color
set-option -g message-style "bg=#686f9a, fg=#ecf0c1"
set-option -g message-command-style "bg=#686f9a, fg=#ecf0c1"
```

### When commands are run

```conf
//- Set color when commands are run
set -g message-style "fg=#0f11b0, bg=#686f9a"
```