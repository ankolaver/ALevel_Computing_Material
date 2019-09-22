def insertion(arr):
    
    for k in range(1,len(arr)):
        temp = k
        while temp>0 and arr[temp-1]>arr[temp]:
            arr[temp-1],arr[temp] = arr[temp],arr[temp-1]
            temp-=1
    print(arr)

array = [3,9,12,1,2,4]
insertion(array)
