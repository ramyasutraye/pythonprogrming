number=int(raw_input())
fact=1
if(fact==0):
    print(1)
else:
    for i in range(1,number+1):
        fact=fact*i
    print fact   
