#! /bin/bash
lscpu -eCPU,CORE | tail -n +2 | sort -h -k2 | head -n$1 | awk '{print "    <vcpupin vcpu=\""NR-1"\" cpuset=\""$1"\"/>"}'
