v=int(input())
w=int(input())
if (w&1==1) or w<2 or w<=v:
    print('invalid input')
else:
        TW=int(((4*v-w)/2))
        FW=int(v-TW)
print(TW,FW)