"""
Slicing strings.
"""

word = "everything"

# Selecting substrings
print(word[1:5]) #for slicing uses indexing this stmt slice from index 1 to 4 (5-1)
print(word[5:9])

# Open ended slices
print(word[5:]) #this stmt slice from index 5 to last char
print(word[:4]) #this stmt slice from index starting char to 3rd char

# Using negative indices
print(word[-3:]) #this stmt slice from index from last 3rd char to last char
print(word[2:-3]) #this stmt slice from index from 3rd char to 3rd from last

# Indexing past the end
print(word[8:20]) # when the slice is not in the bound it will print the chars in the slicing bound
#for outbound it doesnt print anything
print("$" + word[22:29] + "^") #for outbound it doesnt print anything , doesnt throw any error

# Empty slices
print(word[6:6])
print(word[4:2])
#for both it prints nothing
