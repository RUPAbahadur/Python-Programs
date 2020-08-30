"""
for formatting strings
"""

country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)

#format() method is used for formatting
#'{}' is  replacement field where the argument of the format method can be substitute

# '{{}}' this will prints as single brance in output string



mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)
# for more formatting argument number can be given inside the holder for more particular formatting


#for more specific formatting 
name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)

# for more specific formating a colone with number is entered which fix the width of the field regardless how wide the argument is
# symbol which indicates how the field should be aligned: '<' for left aligned,'>' for right aligned, and '^' for centered.


num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)

#for numberic precision f can be for float precision


# to know more about this , can go to this link
#     https://docs.python.org/3.6/library/string.html#formatstrings
