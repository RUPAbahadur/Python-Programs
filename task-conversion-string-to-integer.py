"""
Task-check if the string can be converted to digits and if so return integer otherwise return -1
"""
def check_string(string):
    if(string.isdigit()):
        integer=(int)(string)
    else:
        integer=-1
    return integer

print("Convert string to integer\n===============================")
string=input("Enter the string\n")
print(check_string(string))
