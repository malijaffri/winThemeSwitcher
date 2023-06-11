# Windows Theme Switcher

Windows 10 app to toggle the system color theme (light/dark).

## Usage

The default action on running the executable is to toggle the system Dark Mode. If Light Mode or Dark Mode is explicitly required, it can be selected from the app's Jump List (Windows Start Menu or Taskbar context menu (right-click menu) for the app).

## CLI

Switch between Dark Mode and Light Mode in Windows

### CLI Usage

winThemeSwitcher [ -h | -v | -t | -d | -l ]

If no options are passed, defaults to Toggle

### CLI Options

-h    Display help and exit
-v    Display version info and exit
-t    Toggle current theme
-d    Switch to Dark Mode
-l    Switch to Light Mode

## Dependencies

- darkdetect
- jumplists

## Licence

© 2023 malijaffri. All Rights Reserved.

Distributed under the GNU GPL v3 licence
