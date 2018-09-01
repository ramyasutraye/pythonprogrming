def h(a,n):
    max = a[0]
 
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
    return max
 
a = [1,20,30,45,100]
n = len(a)
m = h(a,n)
print ("h in given array is",m)
