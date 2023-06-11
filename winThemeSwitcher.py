# Import the required libraries
import platform
import sys
from subprocess import run, DEVNULL
from pathlib import Path
from darkdetect import isLight

# OS guard conditions
error = OSError("This script only runs on Windows 10!")
if platform.system() != "Windows":
    raise error
elif platform.release() != "10":
    raise error


"""
# Get resources
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = Path(__file__).parent.resolve()

    return Path(base_path).joinpath(relative_path).resolve()


# Image file path
imgpath = resource_path("favicon.ico")
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
    """
    Pseudo-code

    if run normally or jumplist.selected == "Toggle":
        mode_toggle()
    elif jumplist.selected == "Dark Mode":
        mode_dark()
    else:
        mode_light()
    """
    ...


init()
