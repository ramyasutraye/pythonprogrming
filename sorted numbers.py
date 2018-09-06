arr= [2,1,3]
for i in range(len(arr)):
        for j in range(i+1,len(arr)):
        	if(arr[i]>arr[j]):
        	    a= arr[i]
        	    arr[i]= arr[j]
        	    arr[j]= a
print(arr)        	    
© 2018 GitHub, Inc.
