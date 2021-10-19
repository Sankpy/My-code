even=list()
try:
    x=int(input("Enter the number= "))
    while True:
          if x<=100:
             x=x+1
             if x%2==0:
                even.append(x)
          elif str(x)=='Done' or x>100:break
except:
      print("invalid input")
print(even)
try:
    h=int(input("Enter which number is wanted= "))
    y= even.index(h)
    print(y)
except:
    print("out of range")