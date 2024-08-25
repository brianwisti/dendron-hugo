---
created: '2024-02-10 05:12:51'
description: ''
fname: pub.config.shell.bash
id: qb1dz6jjumzjcnsbaapwtwi
title: Bash
updated: '2024-02-10 05:14:59'
---

I tend to use GNU Bash as my login shell, thanks to its stability.
OTOH I spend more time in Nushell, so haven't paid attention to my Bash setup.

## `bash_profile`

I use my `~/.bash_profile` to set environment variables and load config for assorted
package managers.

For a while there, tmux gave me nested login shells.
This confused `$PATH` handling in all sorts of ways.

```bash
PATH="/usr/bin:/bin:/usr/sbin:/sbin"
source /etc/profile
```

Some little convenience functions for viewing and managing the path.

```bash
showpath() {
  perl -E 'say for split /:/, $ENV{PATH}'
}

pathadd() {
  if [ -d "$1" ] && [[ ":$PATH:" != *":$1:"* ]]; then
    PATH="$1${PATH:+":$PATH"}"
  fi
}
```

Ah, ~Linuxbrew~ Homebrew — the solution to, and cause of, so many shell problems.

```bash
if [ -d "/home/linuxbrew" ] ; then
  # For Homebrew on Linux
  # Output to `/home/linuxbrew/.linuxbrew/bin/brew shellenv`
  eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)

  if [ -d "/home/linuxbrew/.linuxbrew/lib/ruby/gems/3.1.0/bin" ] ; then
    pathadd "/home/linuxbrew/.linuxbrew/lib/ruby/gems/3.1.0/bin"
  fi

  export BREW_PYTHON_HOME="/home/linuxbrew/.linuxbrew/Cellar/python@3.10/3.10.8/libexec/bin"

fi
```

Set a few preferences for openers and editors.

```bash
export PAGER="less -FRX"
export EDITOR=nvim
export NNN_FALLBACK_OPENER=xdg-open
```

Make sure `doom` is available if I've got it that week.

```bash
export DOOM_HOME="$HOME/emacs-configs/emacs-doom"

if [ -d "$DOOM_HOME" ]; then
  pathadd "$DOOM_HOME/bin"
fi
```

## Programming Language Managers

GHCup for Haskell.

```bash
[ -f "$HOME/.ghcup/env" ] && source "$HOME/.ghcup/env"
```

Plenv for managing Perl versions.

```bash
export PLENV_HOME="$HOME/.plenv"

if [ -d "$PLENV_HOME" ]; then
  pathadd "$PLENV_HOME/bin"
fi

if which plenv > /dev/null; then eval "$(plenv init -)"; fi
```

Pyenv for managing Python versions.

```bash
export PYENV_ROOT="$HOME/.pyenv"

if [ -d "$PYENV_ROOT" ]; then
  pathadd "$PYENV_ROOT/bin"
fi

if which pyenv > /dev/null; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  if which pyenv-virtualenv-init > /dev/null; then
    eval "$(pyenv virtualenv-init -)"
  fi
fi
```

Poetry for managing Python projects and their language versions.

```bash
[ -d "$HOME/.poetry/bin" ] && pathadd "$HOME/.poetry/bin"
```

Rakubrew for managing Raku versions.

```bash
export RAKUBREW_HOME="$HOME/.rakubrew"

if [ -d "$RAKUBREW_HOME" ]; then
  pathadd "$RAKUBREW_HOME/bin"
  pathadd "$RAKUBREW_HOME/shims"
  eval "$(rakubrew init Bash)"
fi
```

Rbenv for managing Ruby versions.

```bash
if which rbenv > /dev/null; then
  pathadd "$HOME/.rbenv/shims"
  eval "$(rbenv init - bash)";
fi
```

Cargo for managing Rust versions.

```bash
[ -f "$HOME/.cargo/env" ] && . "$HOME/.cargo/env"
```

Volta for managing Node.js versions and global commands.

```bash
export VOLTA_HOME="$HOME/.volta"

[ -d "$VOLTA_HOME" ] && pathadd "$VOLTA_HOME/bin"
```

Better make sure `~/bin` and `~/.local/bin` are in my path.

```bash
[ -d "$HOME/bin" ] && pathadd "$HOME/bin"
[ -d "$HOME/.local/bin" ] && pathadd "$HOME/.local/bin"
```

Then at the end of the whole thing, if I'm running bash I source my `~/.bashrc`?
Well, okay.
I guess it made sense at the time.

```bash
if [ -n "$BASH_VERSION" -a -n "$PS1" ]; then
  if [ -f "$HOME/.bashrc" ]; then
    . "$HOME/.bashrc"
  fi
fi
```

## `bashrc`

GNU Bash runs this for non-login shells.
So if we aren't running interactively, skip the rest of the file.

```bash
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
```

Manage the command history.
Only include unique commands that don't start with a space.
Append to the history file so it grows over time,
but don't let it get *too* big.

```bash
HISTCONTROL=ignoreboth
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000
```

Check the window size after each command and update the values of LINES and COLUMNS.

```bash
shopt -s checkwinsize
```

I'm accustomed to `**` meaning a recursive match in globs.
Just making sure that carries over to interactive shell sessions.

```bash
shopt -s globstar
```

Track those shell aliases I'm so fond of assembling.

```bash
[ -f ~/.bash_aliases ] && . ~/.bash_aliases
```

Enable tab-completion features in case they weren't already.

```bash
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
```

Add Homebrew completions when I've got that available.

```bash
if which brew &> /dev/null; then
  export BREW_PREFIX=`brew --prefix`
  if [ -f "$BREW_PREFIX/etc/bash_completion" ]; then
    . "$BREW_PREFIX/etc/bash_completion.d/git-completion.bash"
    . "$BREW_PREFIX/etc/bash_completion.d/git-prompt.sh"
    . "$BREW_PREFIX/etc/bash_completion"
  fi
fi
```

Run the `keychain` OpenSSH key manager for my shell sessions.

```bash
if which keychain > /dev/null; then
  eval `keychain --eval --agents ssh id_rsa`
fi
```

Load Direnv hooks if available.

```bash
if which direnv > /dev/null; then eval "$(direnv hook bash)"; fi
```

Load hooks for the `fzf` fuzzy finder.

```bash
[ -f ~/.fzf.bash ] && source ~/.fzf.bash
```

I sometimes have things to run locally that don't need to be in my universal config.

```bash
[ -f ~/.bashrc_local_after ] && . ~/.bashrc_local_after
```

Try to get tmux playing nice with existing sessions.

```bash
if [[ -n "\$PS1" ]] && [[ -z "\$TMUX" ]] && [[ -n "\$SSH_CONNECTION" ]]; then
  tmux attach-session -t remote || tmux new-session -s remote
fi
```

And finally, show my pretty prompt from Starship.

```bash
eval "$(starship init bash)"
```

## `bash_aliases`

Some of these are specific to specific machines.
If I cared more about my GNU Bash setup, I would tidy a bit.

```bash
alias realias='$EDITOR ~/.aliases; source ~/.aliases'

alias bbd='brew bundle dump --force --describe --global'
alias be='bundle exec'
alias blf='beet ls -f "$BF" album+ track+'
alias dnuke='docker kill $(docker ps -q);docker system prune --all --volumes -f'
alias e='emacs -nw'
alias kexp='mplayer http://live-aacplus-64.kexp.org/kexp64.aac'
alias ll='lsd -lF'
alias l='lsd -lahF'
alias ls='lsd'
alias pr='poetry run'
alias pri='poetry run invoke'
alias rire='ripit && beet import ~/mp3 && rmdir ~/mp3 && eject'
alias tsite='task project:Site'
alias tt='task +ticket'
alias ttw='task +ticket +Work +prl'
alias tw='task +Work +prl'
alias unflicker='xrandr --output DisplayPort-0 --mode 2560x1440 --rate 59.95'
alias ymd='date +"%Y%m%d"'
```