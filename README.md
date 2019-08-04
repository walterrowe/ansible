# Ansible Tricks

Python expressions are valid in YAML playbook variable evaluations.

### Accessing Structured Data via Variable

This describes how to use the value of a variable as a key into a structured dictionary to extract values. The concept would be that the variable’s value would be passed into the playbook at run time. In Ansible Tower / AWX, a multiple choice survey can restrict selection to known values.
```
# virtual machine resource profiles
# structured data complex dictionary
#
# vm_specs[‘vm_small’ ].cpu, .ram
# vm_specs[‘vm_medium’].cpu, .ram
# vm_specs[‘vm_large’ ].cpu, .ram
#
# vm_profile: “vm_small”
# vm_specs[vm_profile ].cpu, .ram

vm_profile: vm_small		# guaranteed default value
vm_specs:
  vm_small:
    cpu: 1
    ram: 2
  vm_medium:
    cpu: 2
    ram: 4
  vm_large:
    cpu: 4
    ram: 8

# operating system specific specifications
# structured data complex dictionary
#
# os_specs[‘redhat7’].guest, .scsi, .nic, .image
# os_specs[‘ubuntu’ ].guest, .scsi, .nic, .image
# os_specs[‘windows’].guest, .scsi, .nic, .image
#
# os_profile: “redhat7”
# os_specs[os_profile].guest,.scsi, .nic, .image

os_profile: redhat7		# guaranteed default value
os_specs:
  redhat7:
    guest: rhel7_64bit
    scsi: paravirtual
    nic: vmxnet3
    image: redhat7.iso
  ubuntu:
    guest: ubuntu64bit
    scsi: paravirtual
    nic: vmxnet3
    image: ubuntu18.iso
  windows:
    guest_id: windows9server64bit
    scsi: lsilogicsas
    nic: e1000e
    image: windows16.iso

# filesystems specifications
# structured dictionary of JSON lists
#
# fs_specs[‘general’]
# fs_specs[‘oracle’ ]
# fs_specs[‘mysql’  ]
# fs_specs[‘web’    ]
# fs_specs[‘mssql’  ]
#
# fs_profile: “oracle”
# fs_specs[fs_profile]

fs_profile: general
fs_specs:
  general: [
    { size_gb: 60, type: thin, datastore: somewhere }	# /
  ]
  oracle: [
    { size_gb: 60, type: thin, datastore: somewhere }, 	# /
    { size_tb:  1, type: thin, datastore: somewhere }, 	# /apps
    { size_tb:  1, type: thin, datastore: somewhere } 	# /data
  ]
  mysql: [
    { size_gb: 60, type: thin, datastore: somewhere }, 	# /
    { size_tb:  1, type: thin, datastore: somewhere }, 	# /apps
    { size_tb:  1, type: thin, datastore: somewhere } 	# /data
  ]
  web: [
    { size_gb: 60, type: thin, datastore: somewhere }, 	# /
    { size_gb: 100, type: thin, datastore: somewhere } 	# /sites
  ]
  mssql: [
    { size_gb:  60, type: thin, datastore: somewhere }, # C:
    { size_gb: 100, type: thin, datastore: somewhere }, # D:
    { size_gb: 100, type: thin, datastore: somewhere }, # E:
    { size_gb: 100, type: thin, datastore: somewhere }, # F:
    { size_gb: 100, type: thin, datastore: somewhere }, # G:
    { size_gb: 100, type: thin, datastore: somewhere }, # H:
    { size_gb: 100, type: thin, datastore: somewhere }  # I:
  ]
```
You can loop through two lists in parallel using “with_together”.
```
vms_list:[
  { name:“vm1”, os:“redhat7”, fs:“general”, size:“vm_small” },
  { name:“vm2”, os:“redhat7”, fs:“web”.   , size:“vm_small” },
  { name:“vm3”, os:“redhat7”, fs:“oracle” , size:“vm_large” }
]

mac_addr: [
  “00:00:00:00:00:00”,
  “00:00:00:00:00:00”,
  “00:00:00:00:00:00”
]

# ‘with_together’ syncs two lists into a common list
# [ (a,b) (1,2) ] becomes [ (a,1) (b,2) ]
# item.0 is first item in resulting list (even a list itself)
# item.1 is second item in resulting list (even a list itself)
#
# loop to display vm names, mac addresses
debug:
  msg: VM “{{ item.0.name }}” has MAC address is “{{ item.1 }}”
with_together:
  - “{{ vms_list }}”
  - “{{ mac_addr }}”
```
### String and Variable Operations

Strings in Ansible are strings in Python which are lists of characters. Lists can be concatenated using the “+” operating.
```
var1: “one”
var2: “two”
var3: “three”
var4: “{{ var1 + var2 + var3 }}”
var5: “{{ var1 + ‘ for the money’ }}”
```
The value of var4 is “onetwothree”.
The value of var5 is “one for the money”.

You can split strings with a delimiter.
```
string: “this is a string”
{{ string.split }}		# yields “this”, “is”, “a”, “string”
```
will split on the spaces by default and yield “this”, “is”, “a”, “string”.
```
address: 192.168.100.10
{{ address.split(‘.’) }}	# yields “192”, “160”, “100”, “10”
```
You can split strings with a delimiter and select a specific items from the resulting list.
```
address: 192.168.100.10
{{ address.split(‘.’)[0] }}	# yields “192”
{{ address.split(‘.’)[2] }}	# yields “100”
{{ address.split(‘.’)[-1] }}	# yields “10”
```
And you can use splitext to split a filename on dot to get the basename.
```
filename: basename.iso
{{ address | splitext }}	# yields “basename”
```
You can extract a “substring” using list notation since strings are lists of characters. Remember that lists start with index 0. Substring extract would be specified by index of starting position, a colon, and the number of list items to extract.
```
string: “onetwothree”
{{ string[0:3] }}		# yields “one”
{{ string[3:3] }}		# yields “two”
{{ string[6:5] }}		# yields “three”
{{ string[4:1] }}		# yields “w”
```
This link provides an example of how to build a list in a loop.
https://www.jeffgeerling.com/blog/2017/adding-strings-array-ansible

### Useful References and Examples

Read about Python strings to learn more about Ansible strings.
