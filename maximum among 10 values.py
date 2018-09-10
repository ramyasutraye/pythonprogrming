def max( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max([2,9,4,1,5,10,8,7,6,3]))
