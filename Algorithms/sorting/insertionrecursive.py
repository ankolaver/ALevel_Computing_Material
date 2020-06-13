def insertionsort(arr,i):
    #base case, stop iterating once it reaches end of arr
    if i>0 and i<len(arr):
        key = arr[i]
        temp = i-1
        while temp >= 0 and key < arr[temp]:
            arr[temp+1] = arr[temp]
            temp -= 1 
        arr[temp+1] = key
        #print(arr)
        return insertionsort(arr,i+1)
    else:
       #pass
       print(arr)

item = [5,10,3,1,2,7,7,4]
insertionsort(item,1)
