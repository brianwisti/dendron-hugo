---
created: '2024-02-10 05:09:00'
description: ''
fname: pub.config.shell.fish
id: hxuyzerk8penh8x4qx9ws4n
title: Fish
updated: '2024-02-10 05:09:05'
---

## `config.fish`

```fish
//- file:fish/config.fish
# use status --is-interactive to determine if interactive
# use status --is-login to determine if login shell

set -x COLORTERM truecolor

set -x PATH /usr/bin /bin /usr/sbin /sbin
set -x PATH /usr/local/bin /usr/local/sbin $PATH
set -x PATH /opt/local/sbin /opt/local/bin $PATH

set -x EDITOR nvim

set CARGO_BIN ~/.cargo/bin
set DART_LIB /usr/lib/dart
set EMACS_BIN ~/.emacs.d/bin
set KITTY_HOME $HOME/.local/kitty.app
set LINUXBREW_HOME /home/linuxbrew/.linuxbrew/bin
set HOMEBREW_BUNDLE_FILE ~/.dotfiles/Brewfile
set POETRY_HOME $HOME/.poetry
set RAKUBREW_HOME ~/.rakubrew/


set -U FZF_DEFAULT_COMMAND 'fd --type f --hidden --follow --exclude .git'
set -U FZF_FIND_FILE_COMMAND 'fd --type f --hidden --follow --exclude .git . \$dir'
set -U FZF_CTRL_T_COMMAND $FZF_DEFAULT_COMMAND

if test -d $LINUXBREW_HOME
  set -x PATH $LINUXBREW_HOME $PATH
  set -Ux BREW_PREFIX (brew --prefix)
  set BREW_PYTHON_HOME "$BREW_PREFIX/Cellar/python@3.9/3.9.0/libexec/bin"

  if test -d $BREW_PYTHON_HOME
    set -gx PATH $BREW_PYTHON_HOME $PATH
  end
end

if test -d $DART_LIB
  set -x PATH $DART_LIB/bin $PATH
end

if test -d $EMACS_BIN
  set -x PATH $EMACS_BIN $PATH
end

if test -d $KITTY_HOME
  set -x PATH $KITTY_HOME/bin $PATH
  # Kitty not picking this up in Awesome?
  set -x KITTY_CONFIG_DIRECTORY ~/.config/kitty
end

if test -d $RAKUBREW_HOME
  $RAKUBREW_HOME/bin/rakubrew init Fish | source
end

if test -d $POETRY_HOME
  set -x PATH $POETRY_HOME/bin $PATH
end

if test -d $CARGO_BIN
  set -x PATH $CARGO_BIN $PATH
end

if test -d ~/bin
  set -x PATH ~/bin $PATH
end

#if status --is-interactive
#  keychain --eval --agents ssh id_rsa randomgeek_rsa | source
#end

if test -d ~/.asdf
  source ~/.asdf/asdf.fish
end

source ~/.config/fish/aliases.fish

eval (direnv hook fish)

starship init fish | source
set -gx VOLTA_HOME "$HOME/.volta"
set -gx PATH "$VOLTA_HOME/bin" $PATH
```

## `aliases.fish`

```fish
//- file:fish/aliases.fish
alias rgpy 'rg --type=py'
alias bbd 'brew bundle dump --force --describe --global'
alias be 'bundle exec'
alias e 'emacs -nw'
alias kexp 'mplayer http://live-aacplus-64.kexp.org/kexp64.aac'
alias ls 'lsd'
alias ll 'lsd -la'
alias pr 'poetry run'
alias pri 'poetry run invoke'
alias realias "$EDITOR ~/.config/fish/aliases.fish; source ~/.config/fish/aliases.fish"
alias rire 'ripit && beet import ~/mp3 && rmdir ~/mp3 && eject'
alias tlema 'task project:Lema +Work'
alias tilema 'task project:Lema +Work +issue'
alias ttlema 'task project:Lema +Work +ticket'
alias tn 'task-note'
alias tickets 'task +ticket'
alias unflicker 'xrandr --output DP-1 --mode 2560x1440 --rate 59.95'
alias work 'task +Work'
alias ymd 'date +"%Y%m%d"'
```