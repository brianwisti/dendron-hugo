---
created: '2024-02-10 05:21:51'
description: ''
fname: pub.config.linux.qtile
id: i7qg1ynju5g0n985i5cvshg
title: Qtile
updated: '2024-08-03 02:25:38'
---

Still learning my way, so think of it more as annotation for the default config.

## `config.py`

This is the entry point for a Qtile session.

Do system imports.

```python
import os
```

Import the useful bits from my config modules.

```python
from modules import const
from modules.groups import groups
from modules.hooks import *
from modules.keys import keys, mod
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens
```

I don't like that `import *`.
Gonna see if I *really* need to do it that way.

```python
dgroups_key_binder = None
dgroups_app_rules = []  # type: List

follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"
widget_defaults = dict(
        font=const.FONT_FAMILY_FIXED,
        fontsize=13,
        padding=3
)
```

## Modules

### `__init__.py`

Probably going overboard on the literate config.

```python
# This space intentionally left blank.
```

### `const.py`

This holds constants — which may become fallback defaults someday.
Regardless, the main point is so my config includes fewer [magic values][magic].

[magic]: https://kyleshevlin.com/what-are-magic-values

```python
FONT_FAMILY_FIXED = "Fira Code"
FONT_FAMILY_PROSE = "Atkinson Hyperlegible"
```

### `groups.py`

Or screens, or virtual desktops.

#### Imports

```python
from libqtile.command import lazy
from libqtile.config import Key, Group

from .keys import keys, mod
```

#### Define Screen Groups

The defaults use a simple numbering scheme for its nine groups.

```python
groups = [Group(i) for i in "123456789"]
```

#### Add keybindings for each group

- <kbd>Mod+n</kbd> switches to group `<n>`
- <kbd>Mod+Shift+n</kbd> moves currently focused window to group `n`
- <kbd>Mod+Right</kbd> switches to the group right of current (2 → 3, etc)
- <kbd>Mod+Left</kbd> switches to the group left of current (2 → 1, etc)

The directional switches wrap around.
Group 1 is to the right of group 9, and group 9 is to the left of group 1.

```python
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod], "Right", lazy.screen.next_group(),
            desc="Switch to next group"),

        Key([mod], "Left", lazy.screen.prev_group(),
            desc="Switch to previous group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])
```

### `hooks.py`

Hooks specific functions to specific Qtile events.

#### Imports for hooks

```python
import os
import subprocess

from libqtile import hook
```

#### Run `autostart.sh` once on startup

```python
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
```

### `keys.py`

Global keybindings and some defaults.

#### Imports for key bindings

```python
from libqtile.config import Key
from libqtile.lazy import lazy
```

#### Define some defaults

The `mod4` key is the logo key —
usually a Windows logo on most keyboards I see.

```python
mod = "mod4"
```

My preferred terminal emulator is WezTerm.

```python
terminal = "wezterm"
```

#### Define keybindings

Just dumping the defaults for now.
We have company on the way.

```python
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "r", lazy.spawn("rofi -show combi"), desc="spawn rofi"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume",lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume",lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute",lazy.spawn("amixer set Master toggle")),
]
```

### `layouts.py`

My preferred layouts for Qtile on my ridiculously wide monitor.

- Columns
- MonadThreeCol
- Floating

Other built-in options that I may evaluate later:

- MonadTall
- Stack
- Bsp
- Matrix
- MonadTall
- MonadWide
- RatioTile
- Tile
- TreeTab
- VerticalTile
- Zoomy

```python
from libqtile import layout
from libqtile.config import Match

layouts = [
    layout.Columns(border_focus_stack='#d75f5f'),
    layout.MonadThreeCol(),
]
```

And then a floating layour because some application windows work best floating.

```python
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
```

### `mouse.py`

What happens when you click a mouse button or tap the trackpad.

```python
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from .keys import mod

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
```

### `screens.py`

How the screen is laid out: taskbars and stuff like that.

```python
import os

from libqtile import bar
from libqtile.config import Screen

from modules.keys import terminal
from .widgets import *

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f", mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"), 
                widget.GroupBox(
                                highlight_method='line',
                                this_screen_border="#5294e2",
                                this_current_screen_border="#5294e2",
                                active="#ffffff",
                                inactive="#848e96",
                                background="#2f343f"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.CheckUpdates(
                    update_interval=1800,
                    distro="Arch_yay",
                    display_format="{updates} Updates",
                    foreground="#ffffff",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(terminal + ' -e yay -Syu')
                    },
                    background="#2f343f"),
                widget.Systray(icon_size = 20),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f'
                       ),    
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p',
                             background="#2f343f",
                             foreground='#9bd689'),
                widget.TextBox(                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#2f343f',
                       ),   
                widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                )
                
            ],
            30,  # height in px
            background="#404552"  # background color
        ), ),
]
```

### `widgets.py`

Custom widgets for the Qtile desktop.

#### Imports for widgets

```python
from libqtile import qtile, widget

from modules import const
```

#### Theme colors

```python
colors = [
    ["#282c34", "#282c34"], # panel background
    ["#3d3f4b", "#434758"], # background for current screen tab
    ["#ffffff", "#ffffff"], # font color for group names
    ["#ff5555", "#ff5555"], # border line color for current tab
    ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
    ["#e1acff", "#e1acff"], # window name
    ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
]
```

#### Widget Defaults

```python
widget_defaults = dict(
    font=const.FONT_FAMILY_PROSE,
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
```

#### Volume Control Widget

```python
class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        # drawing here crashes Wayland

    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = ''
        elif self.volume <= 15:
            self.text = ''
        elif self.volume < 50:
            self.text = ''
        else:
            self.text = ''
        self.draw()

        if wob:
            with open(self.wob, 'a') as f:
                f.write(str(self.volume) + "\n")
```

The defaults initialize a MyVolume widget off in the widgets library.

```python
volume = MyVolume(
    fontsize=18,
    font='Font Awesome 5 Free',
    foreground=colors[4],
    background='#2f343f',
    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")}
)
```

## `autostart.sh`

Fires up tasks and applications which should run for every session. I skip the battery check from the default setup since I am running on a plugged-in desktop.

```sh
#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/endeavouros-wallpaper.png
picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
```