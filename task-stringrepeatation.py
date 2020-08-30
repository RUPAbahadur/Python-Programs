"""
Task- to display repeatation of the string
"""
def echo(string, repeatation_times):
    result=string+('\n'+ string)*(repeatation_times-1)
    print(result)

print("Enter the string and the number of repeatation times\n======================================")
string=input("Enter the string:\n")
repeatation_times=int(input("Enter the repeatation times:\n"))
echo(string, repeatation_times)


