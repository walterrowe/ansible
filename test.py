#!/usr/local/bin/python3

##
## https://linuxhint.com/python_scripts_beginners_guide/
##
import sys, re

# Define a dictionary
machines = {
    't2.small'  : { 'cpu':1, 'ram':2 },
    't2.medium' : { 'cpu':2, 'ram':4 },
    't2.large'  : { 'cpu':4, 'ram':8 }
}

if len(sys.argv) > 1:
    sizes = sys.argv[1:]
else:
    size = input("Enter a machine size(s) separated by commas: ")
    sizes = re.split('\s*[,]\s*',size)

for size in sizes:
    print (size)

# test dict.get()
for size in sizes:
    if size in machines.keys():
        print ("Machine Size",size,"has",machines[size]['cpu'],"CPUs and",machines[size]['ram'],"GB RAM")
    else:
        print ("Invalid machine size.")
