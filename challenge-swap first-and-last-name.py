"""
Challenge - to swap first and last name
"""
def swap(full_name):
    (first_name,last_name)=full_name.split(" ")
    return last_name.capitalize() + " " + first_name.capitalize()

print("To swap first and last name\n================================")
full_name=input("Enter your full name:\n")
print(swap(full_name))
