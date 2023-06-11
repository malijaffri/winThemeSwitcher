# Import the required libraries
import platform, sys, getopt, jumplists
from subprocess import run, DEVNULL
from pathlib import Path
from darkdetect import isLight

# OS guard conditions
platerror = OSError("This script only runs on Windows 10!")
if platform.system() != "Windows":
    raise platerror
elif platform.release() != "10":
    raise platerror


# Version
version = "v0.1.0"

# Help string
helpstr = f"""
winThemeSwitcher {version}

Switch between Dark Mode and Light Mode in Windows

Usage:
winThemeSwitcher [ -h | -v | -t | -d | -l ]

If no options are passed, defaults to Toggle

Options:
-h    Display this help and exit
-v    Display version info and exit
-t    Toggle current theme
-d    Switch to Dark Mode
-l    Switch to Light Mode
"""

# Theme variable names
themeTypes = ("SystemUsesLightTheme", "AppsUseLightTheme")

# Stringified command list with variables
# Use with `eval`
#
# Vars used:
# - `mode`: str, '0' or '1'
# - `themeType`: str, one of `themeTypes`
command = '["reg.exe", "add", "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize", "/v", themeType, "/t", "REG_DWORD", "/d", mode, "/f"]'


def error():
    print(helpstr)
    sys.exit(2)


# Set color mode
def mode_set(mode: int | str):
    mode = str(mode)
    if mode not in ("0", "1"):
        raise ValueError(
            f"Parameter 'mode' must be either 0 or 1! Provided value: {mode}"
        )
    for themeType in themeTypes:
        run(eval(command), stdout=DEVNULL, stderr=DEVNULL)


# Set Dark theme
def mode_light():
    mode_set(1)


# Set Dark theme
def mode_dark():
    mode_set(0)


# Toggle current theme
def mode_toggle():
    mode_dark() if isLight() else mode_light()


# Initialise switcher
def init():
    ...


def main(argv):
    # init()
    opts, args = [], []
    try:
        opts, args = getopt.getopt(argv, "hvtdl")
    except getopt.GetoptError:
        error()
    if len(opts) > 1:
        error()
    if args:
        error()
    if not opts:
        mode_toggle()
        sys.exit()
    opt, arg = opts[0]
    match opt:
        case "-h":
            print(helpstr)
        case "-v":
            print(version)
        case "-t":
            mode_toggle()
        case "-d":
            mode_dark()
        case "-l":
            mode_light()
        case _:
            error()
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
