massage="Alexa don't find the answer"
string_list=massage.split()
count=0
for i in string_list:
    for j in i:
        if j=='A' or j=='e' or j=='i'or j=='o' or j=='u' or j=='a':
           count+=1
print(count)
print('done')