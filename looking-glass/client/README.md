# [Looking Glass Client](https://looking-glass.hostfission.com/)
[Github project](https://github.com/gnif/LookingGlass)
## .looking-glass-client.ini
A simple `looking-glass-client` config. Move it to one of the locations below if you intend to use the `win` script to start `looking-glass-client` and `scream`. The looking-glass-client looks for configs in 2 default locations:
- `/etc/looking-glass-client.ini`
- `~/.looking-glass-client.ini`

## win
The script must be modified to your use. Feel free to rename it as you see fit. The name makes little difference if combined with the desktop launcher. Make sure `VIRT_BRIDGE` AND `WINDOWS_DOMAIN` are set correctly for your VM name and host bridge interface. Move it to `~/.local/bin/win` and `chmod +x ~/.local/bin/win` to use it.

## Windows.desktop
Drop in `~/.local/share/applications/` to have a desktop application launcher for `win`. Make sure to assign/update the icon to something you like.
