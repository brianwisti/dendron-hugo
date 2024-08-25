---
created: '2024-02-10 05:10:52'
description: ''
fname: pub.config.shell.zsh
id: h9yg7wv0u9rwbve1bivfkcx
title: Zsh
updated: '2024-02-10 05:10:56'
---

I don't use Zsh much at the moment. These files are in for the sake of completeness. That way I have all my dotfiles in this collection. But consider it untested while this warning is up.

## `zshenv`

```zsh
//- file:zshenv
# Runs in all sessions

export CARGO_HOME="$HOME/.cargo"
export CLICOLOR=1
export DOOM_HOME="$HOME/.emacs.doom.d"
export EDITOR="nvim"
export GOPATH="$HOME/go"

# See brian d foy's "Preparing for Perl 7"
# export PERL5OPT="-Mv5.32 -Mstrict -Mwarnings \
#   -Mfeature=signatures -M-warnings=experimental::signatures \
#   -M-feature=indirect \
#   -M-bareword::filehandles \
#   -M-multidimensional"
export PLENV_HOME="$HOME/.plenv"
export PYENV_ROOT="$HOME/.pyenv"
export PYENV_HOME_BIN="$HOME/.pyenv/bin"

# Starship takes care of this for me.
export PYENV_VIRTUALENV_DISABLE_PROMPT=1

export RBENV_HOME="$HOME/.rbenv"
export VOLTA_HOME="$HOME/.volta"
export DOTNET_ROOT="/usr/local/opt/dotnet/libexec"

eval "$(/Users/random/.rakubrew/bin/rakubrew init Zsh)"

if [[ -d "$CARGO_HOME" ]]; then
  source "$HOME/.cargo/env"
fi


if [ -e /home/random/.nix-profile/etc/profile.d/nix.sh ]; then . /home/random/.nix-profile/etc/profile.d/nix.sh; fi # added by Nix installer
. "$HOME/.cargo/env"
if [ -n "$PYTHONPATH" ]; then
    export PYTHONPATH='/opt/homebrew/Cellar/pdm/2.2.1/libexec/lib/python3.11/site-packages/pdm/pep582':$PYTHONPATH
else
    export PYTHONPATH='/opt/homebrew/Cellar/pdm/2.2.1/libexec/lib/python3.11/site-packages/pdm/pep582'
fi
```

## `zshrc`

```zsh
//- file:zshrc
bindkey -e

export PATH="/opt/homebrew/opt/bison/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/bison/lib"

export LDFLAGS="-L/opt/homebrew/opt/libffi/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libffi/include"

export PKG_CONFIG_PATH="/opt/homebrew/opt/libffi/lib/pkgconfig"

vterm_printf(){
    if [ -n "$TMUX"  ]; then
        # Tell tmux to pass the escape sequences through
        #
        # (Source: http://permalink.gmane.org/gmane.comp.terminal-emulators.tmux.user/1324)
        #
        printf "\ePtmux;\e\e]%s\007\e\\" "$1"
    elif [ "${TERM%%-*}" = "screen"  ]; then
        # GNU screen (screen, screen-256color, screen-256color-bce)
        #
        printf "\eP\e]%s\007\e\\" "$1"
    else
        printf "\e]%s\e\\" "$1"
    fi
}

# ssh keychain manager
if which keychain > /dev/null; then eval `keychain --eval --agents ssh id_rsa`; fi

if which plenv > /dev/null; then eval "$(plenv init - zsh)"; fi

if which pyenv > /dev/null; then
  eval "$(pyenv init --path)"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi

if which rbenv > /dev/null; then
  eval "$(rbenv init -)"
fi

if [[ -d "$HOME/.rakubrew" ]]; then eval "$($HOME/.rakubrew/bin/rakubrew init Zsh)"; fi

if which direnv > /dev/null; then eval "$(direnv hook zsh)"; fi

BROOT_LAUNCHER="~/.config/broot/launcher/bash/br"

if [[ -e "$BROOT_LAUNCHER" ]]; then
  source "$BROOT_LAUNCHER"
fi

source "$HOME/.aliases"
eval "$(starship init zsh)"

export PATH="$HOME/.poetry/bin:$PATH"
export PATH="$HOME/apps/sublime_text:$PATH"
export PATH="$HOME/.config/composer/vendor/bin:$PATH"

if [[ -e $HOME/.asdf/asdf.sh ]]; then
  . $HOME/.asdf/asdf.sh
fi


[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
export PATH="/Applications/WezTerm.app/Contents/MacOS:$PATH"

export VOLTA_HOME="$HOME/.volta"
export PATH="$VOLTA_HOME/bin:$PATH"
```

## `zprofile`

```zsh
//- file:zprofile
# Apple does weird things to path after I define it in zshenv, so define it here instead.
#zmodload zsh/pcre

# setopt REMATCH_PCRE

typeset system_paths=(
  "/usr/local/bin"
  "/Applications/Postgres.app/Contents/Versions/latest/bin"
  "/Library/Frameworks/Mono.framework/Versions/Current/Commands"
  "/Applications/Keybase.app/Contents/SharedSupport/bin"
  "/Library/Apple/usr/bin"
  "/usr/sbin"
  "/usr/bin"
  "/bin"
)

typeset macports_paths=(
  "/opt/local/sbin"
  "/opt/local/bin"
)

typeset linux_paths=(
  "/snap/bin"
)

typeset app_paths=()

if [[ -d "$PYENV_HOME_BIN" ]]; then app_paths+="$PYENV_HOME_BIN"; fi

if [[ -d "$DOOM_HOME" ]]; then app_paths+="$DOOM_HOME/bin"; fi

if [[ -d "$VOLTA_HOME" ]]; then app_paths+="$VOLTA_HOME/bin"; fi

if [ -d "/home/linuxbrew" ] ; then
  # For Homebrew on Linux
  linux_paths+=(
    "/home/linuxbrew/.linuxbrew/bin"
    "/home/linuxbrew/.linuxbrew/sbin"
  )
  # Output to `/home/linuxbrew/.linuxbrew/bin/brew shellenv`
  eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)

  if [[ -e $(brew --prefix asdf)/asdf.sh ]]; then
    . $(brew --prefix asdf)/asdf.sh
  fi
fi

if [ -d "$HOME/.local/bin" ] ; then app_paths+=("$HOME/.local/bin"); fi

if [ -d "/usr/local/go" ]; then app_paths+=("/usr/local/go/bin"); fi

if [ -d "$HOME/bin" ] ; then app_paths+=("$HOME/bin"); fi

if [ -d "$HOME/.perl6/bin" ] ; then app_paths+=("HOME/.perl6/bin"); fi

if [ -d "$PLENV_ROOT" ] ;
  then app_paths+=("$PLENV_ROOT/bin");
  eval "$(pyenv init --path)"
fi

if [ -d "$RBENV_HOME" ] ; then app_paths+=("$RBENV_HOME/bin"); fi

app_paths+=("$HOME/.poetry/bin")
app_paths+=("$HOME/.emacs.d/bin")

if [ -d "$CARGO_HOME" ]; then app_paths+="$CARGO_HOME/bin"; fi

if [ -d "$DOOM_HOME" ]; then app_paths+="$DOOM_HOME/bin"; fi

if [[ "$OSTYPE" =~ "darwin" ]]; then
  path=($app_paths $macports_paths $system_paths)
else
  export PKG_CONFIG_PATH="/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/share/pkgconfig"

  path=($app_paths $linux_paths $system_paths)
fi


source "$HOME/.aliases"

# MacPorts Installer addition on 2020-12-27_at_21:06:54: adding an appropriate DISPLAY variable for use with MacPorts.
export DISPLAY=:0
# Finished adapting your DISPLAY environment variable for use with MacPorts.

eval "$(/opt/homebrew/bin/brew shellenv)"
```