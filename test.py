##
## https://linuxhint.com/python_scripts_beginners_guide/
##
# Define a dictionary
customers = {
    '06753':'Mehzabin Afroze',
    '02457':'Md. Ali', 
    '02834':'Mosarof Ahmed',
    '05623':'Mila Hasan',
    '07895':'Yaqub Ali'
    }

# Append a new data
customers['05634'] = 'Mehboba Ferdous'

print("The customer names are:")
# Print the values of the dictionary
for customer in customers:
    print(customers[customer])

# Take customer ID as input to search
name = input("Enter customer ID:")

# Search the ID in the dictionary
found = False
for customer in customers:
    if customer == name:
        found = True
        print("1. Customer",name,"is",customers[customer])
        break
if not Found:
    print("1. Customer",name,"not found.")


# Search the ID in the dictionary
# test dict.keys()
if name in customers.keys():
    print("2. Customer",name,"is",customers[name])
else:
    print("2. Customer",name,"not found.")

# test dict.setdefault()
print("3. Customer",name,"is",customers.setdefault(name))

# test dict.get()
print("4. Customer",name,"is",customers.get(name,"not found."))
