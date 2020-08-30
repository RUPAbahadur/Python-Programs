"""
String indexing examples.
"""

phrase = "Python is great!"

# first character
print(phrase[0]) #retrieve the first char of variable'a value

# fourth character
fourth = phrase[3]
print(fourth)
print(type(phrase)) # 'type' returns the type of object ->str
print(type(fourth)) # in python even a single character is considered as a str type

# length of string
phraselen = len(phrase) #returns no.of. character)starts from 1) #indexing starts from 0
print(phraselen)


# last character
print(phrase[phraselen - 1]) #to retrieve last char -1 can be used
print(phrase[-1])       #indexing from left: 0 1 2 3 ...
                        #indexing from right: .....-3 -2 -1
    
# thirteenth from last (fourth) character
print(phrase[-13])

# Out of bounds
#print(phrase[phraselen]) #index should be in range not more not less
#print(phrase[-20])

# Indices
# string = "abcde"
# character   a  b  c  d  e
# pos index   0  1  2  3  4
# neg index  -5 -4 -3 -2 -1
