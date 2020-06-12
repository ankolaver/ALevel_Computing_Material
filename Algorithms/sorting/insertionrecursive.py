def insertionsort(arr,i):
    if i>0 and i<len(arr):
        key = arr[i]
        temp = i-1
        while temp >= 0 and key < arr[temp]:
            arr[temp+1] = arr[temp]
            temp -= 1 
        arr[temp+1] = key
        print(arr)
        return insertionsort(arr,i+1)
