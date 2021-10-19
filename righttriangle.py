rightangle=list()
x=int(input("Enter the number= "))
try:
    while True:
        if x<=10:
             rightangle.append(x)
             x=x+1
             print(rightangle)
        elif x>10:break
except:
       print('invalid input')