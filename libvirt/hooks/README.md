# [Hooks](https://libvirt.org/hooks.html)
These are scripts that libvirt will call when a guest is required to perform specific operations. There are hooks for a number of services including QEMU, LXC, Network etc. Scripts for the specific service should be named after the service they intend to hook.

## [QEMU](https://libvirt.org/hooks.html#qemu)
This hook is intended to load/unload the `vfio-pci` driver for the GPU being passed to the guest.

Adjust the device IDs to match your specific GPU/Sound device.

Place this script in `/etc/libvirt/hooks/`.