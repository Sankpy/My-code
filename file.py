file_handler=input('enter the file name= ')
if len(file_handler)<1:file_handler='mbox-short.txt'
fh=open(file_handler)
count=0
email='None'
email_list=list()
for lines in fh:
    lines=lines.strip()
    if  lines.startswith('From'):
        words=lines.split()
        if email==words[1]:continue
        email=words[1]
        count=count+1
        print(email)
        email_list.append(email)
print("There is",count,"emails") 
try:
    search_file=input("search email: ")
    print(email_list.index(search_file))
except:
    print('invalid input')