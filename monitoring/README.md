# Monitoring
Tools for monitoring your VFIO host.

## raid_status.py
This is a very rough script to convert *most* of the output from `mdadm --detail /dev/md<num>` to json, pretty dictionary, or a table. It's primary function is to report raid status to display in conky.