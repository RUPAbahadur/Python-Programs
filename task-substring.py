"""
Task-to find if the substring is present in the given string
"""
def is_substring_in_string(string, sub_string):
    result=sub_string in string
    if(sub_string in string):
        return "Substring is present in the string"
    else:
        return "Substring is not present in the string"
    

    
print("To find whether the  substring is present in the stirng\n==================================")
string=input("Enter the string:\n")
sub_string=input("Enter the substring:\n")
print(is_substring_in_string(string, sub_string))

