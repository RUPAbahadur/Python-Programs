"""
Simple string literal examples.
"""

# Strings are enclosed in quotes
name = 'Scott Rixner' #strings should be enclosed in quotes either single quotes or double
university = "Rice"

print(name)
print(university)

# Multiline strings use triple quotes
address = '''Rice University
Houston, TX
'''

# First Fig by Edna St. Vincent Millay
poem = """My candle burns at both ends;
  It will not last the night;
But ah, my foes, and oh, my friends---
  It gives a lovely light!
"""

print("")

print("Address")
print("=======")
print(address)

print("First Fig")
print("=========")
print(poem)


# Characters
#string type can have alphanumberic and even symbols as values
chars = "abc'DEF*&$"
print(chars)
chars2 = '\t"abc"\ndef\'' #uses different quotes  for difference
print(chars2)

# String "arithmetic"
print("Concatenating strings")
name_and_uni = name + " " + university # '+' used for concatenation 
print(name_and_uni)

print("")
print("")
print("Repeating strings")
lots_o_rice = university * 4 #'*' used for repeating 
print(lots_o_rice)

# Using str
num = 3.87
strnum = str(num) # 'str' is like typecasting , convert anything into string
print("number: " + strnum)
# print("number: " + num) # this line will throw error since we cannot add string with other types
# to make above one to run we need to typecast any of them to other type 
