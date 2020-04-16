# Tuning
Tools and utilities to aid in squeazing more performance from your VFIO host and/or VM(s).

## cpu_pinning.sh
This script accepts one argument for the number of cores to consider and produces the `<vcpupin>` stanza with matching each "CORE" to it's associated "CPU". The goal is to pin cores that are physically near eachother (on the same core) and not allow the VM to send work to other CPUs on different cores.
For example, given the following CPU topography:
```bash
$ lscpu -eCPU,CORE
CPU CORE
  0    0
  1    1
  2    2
  3    3
  4    4
  5    5
  6    6
  7    7
  8    8
  9    9
 10   10
 11   11
 12   12
 13   13
 14   14
 15   15
 16    0
 17    1
 18    2
 19    3
 20    4
 21    5
 22    6
 23    7
 24    8
 25    9
 26   10
 27   11
 28   12
 29   13
 30   14
 31   15
 ```
 If you want to assign 2 CPUs to the VM you would ideally choose CPU #1 and # 16 because they are both on core #0.

 If you wanted to assign 4 CPUs, then you would choose CPUs #0, #16, #1, #17.

 Usage:
 ```bash
$ ./cpu_pinning.sh 16
    <vcpupin vcpu="0" cpuset="0"/>
    <vcpupin vcpu="1" cpuset="16"/>
    <vcpupin vcpu="2" cpuset="1"/>
    <vcpupin vcpu="3" cpuset="17"/>
    <vcpupin vcpu="4" cpuset="18"/>
    <vcpupin vcpu="5" cpuset="2"/>
    <vcpupin vcpu="6" cpuset="19"/>
    <vcpupin vcpu="7" cpuset="3"/>
    <vcpupin vcpu="8" cpuset="20"/>
    <vcpupin vcpu="9" cpuset="4"/>
    <vcpupin vcpu="10" cpuset="21"/>
    <vcpupin vcpu="11" cpuset="5"/>
    <vcpupin vcpu="12" cpuset="22"/>
    <vcpupin vcpu="13" cpuset="6"/>
    <vcpupin vcpu="14" cpuset="23"/>
    <vcpupin vcpu="15" cpuset="7"/>
 ```
