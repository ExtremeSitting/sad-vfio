#! /bin/bash
read -p "Num Cores: " CORES
lscpu -eCPU,CORE | tail -n +2 | sort -h -k2 | head -n$CORES | awk -p '{print "    <vcpupin vcpu=\""NR-1"\" cpuset=\""$1"\"/>"}'
