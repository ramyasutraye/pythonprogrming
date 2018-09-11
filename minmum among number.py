def min( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(min([2,9,4,1,5,10,8,7,6,3]))
