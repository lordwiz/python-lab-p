string = input('Enter a string')
if string.endswith('ing'):
    string+='ly'
elif len(string)>=3:
    string+='ing'
print(string)
