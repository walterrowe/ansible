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
for customer in customers:
    if customer == name:
        print(customers[customer])
        break
        
# Search the ID in the dictionary
if name in customers.keys():
    print("1. Customer",name,"is",customers[name])
else:
    print("1. Customer",name,"not found.")

print("2. Customer",name,"is",customers.setdefault(name))
print("3. Customer",name,"is",customers.setdefault(name,'not found.'))
