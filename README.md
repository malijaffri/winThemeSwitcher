# Windows Theme Switcher

Windows 10 system tray app to toggle the system color theme (light/dark).

## Usage

After running the executable, the app will start running in the Windows system tray. The actions can be accessed by opening the tray icon's context menu (right-click on a standard mouse).

There are 3 actions that can be performed:

- Toggle: Toggle the system Dark Mode by either clicking the tray icon or clicking "Toggle" in the context menu.
- Light Mode: Explicitly set Light Mode by selecting it in the context menu.
- Dark Mode: Explicitly set Dark Mode by selecting it in the context menu.
- Quit: Quit the app.

If desired, the app can be set to run at system startup by adding a shortcut to the executable to the `shell:startup` folder. This folder can be accessed by executing `shell:startup` in Windows Run (`Windows Key` + `R`) or entering `shell:startup` in the Windows Explorer address bar. You can also manually navigate to `%userprofile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`.

## Dependencies

- pystray
- darkdetect
- Pillow

## Licence

© 2023 malijaffri. All Rights Reserved.

Distributed under the GNU GPL v3 licence
