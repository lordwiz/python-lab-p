test_str = input('Enter a string')
all_frq={}
for i in test_str:
 if i in all_frq:
  all_frq[i]+=1
 else:
  all_frq[i]=1
print("The number of characters in " ,test_str, " is :" ,str(all_frq))
