def div(Number):
        Number=int(input("enter= "))
        count=0
        divicible=list()
        while count<Number:
             if count%3==0:
                divicible.append(count)
             count=count+1
        print(divicible)
div('Number')
     
          