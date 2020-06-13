def recursivebubble(arr,i):
    if len(arr)>1 and i<len(arr):
        swapmulti = False
        for k in range(0, len(arr)-i):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1] = arr[k+1], arr[k]
                swapmulti = True
        
        else:
            return recursivebubble(arr,i+1)
    else:
        return arr
