"""
String searching examples.
"""
# '+' used for concatenation and '\' backslach is used to tell the interpreted that treat them as same line

sentence = "When I tell you pick up the " + \
           "left rock, it will be the " + \
           "right one, and then only " + \
           "the right rock will be left."

# Finding strings within strings
print("Finding lefts")
firstleft = sentence.find("left") #var.find("tobefound") , find is used to find the first occurence
#return the index of first occurence
print(firstleft, sentence[firstleft])
lastleft = sentence.rfind("left") #var.rfind("tobefound") , rfind is used to find the last occurence
#return the index of last occurence
print(lastleft, sentence[lastleft])

print("")
print("Finding rights")
firstright = sentence.index("right") #var.index("tobefound") , index is used to find the first occurence
# return the index of first occurence
print(firstright, sentence[firstright])
lastright = sentence.rindex("right") #var.rindex("tobefound")
#index is used to find the last occurence - return the index of first occurence
print(lastright, sentence[lastright])

#difference b/w find and index is that when the word is not found
#find will return -1 but index will throw an error

print("")
print("Finding Rixner")
firstrixner1 = sentence.find("Rixner")
print(firstrixner1)
# firstrixner2 = sentence.index("Rixner")
# print(firstrixner2)

# Counting strings within strings
print("")
print("Counting substrings")
print("Number of lefts:", sentence.count("left"))
# var.count("word") is used to find the count or no. of.time the word occured 
# count() this will return the number of occurence , if word not found will return -->0
print("Number of apples:", sentence.count("apple"))
# Checking start/ends
print("")
print(sentence.startswith("When"))
# var.startwith("word") is used to find whether the string starts with particular word
# if so than returns true ortherwise returns false
print(sentence.endswith("The end."))
# var.endwith("word") is used to find whether the string endwith with particular word
# if so than returns true ortherwise returns false
