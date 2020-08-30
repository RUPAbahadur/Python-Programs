"""
Task- to make a name tag
"""
def greet(string, age):
    if(age>=18):
        answer="So you are major."
    else:
        answer="So you are minor."
    greeting="Hello {}. {}" 
    return greeting.format(string, answer)
    
string=input("May I know your name?\n")
age=int(input("and how old are you?\n"))
print(greet(string, age))
