##
## https://linuxhint.com/python_scripts_beginners_guide/
##
# Define a dictionary
machines = {
    't2.small'  : { 'cpu':1, 'ram':2 },
    't2.medium' : { 'cpu':2, 'ram':4 },
    't2.large'  : { 'cpu':4, 'ram':8 }
}

for size in machines:
    print ("Machine Size",size,"has",machines[size]['cpu'],"CPUs and",machines[size]['ram'],"GB RAM")

size = input("Enter a machine size: ")

# test dict.get()
if size in machines.keys():
    print ("Machine Size",size,"has",machines[size]['cpu'],"CPUs and",machines[size]['ram'],"GB RAM")
else:
    print ("Invalid machine size.")
