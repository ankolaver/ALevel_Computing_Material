def mergesort(arr):
    #print(arr)
    if len(arr)>1:
        mid = len(arr)//2
        low = arr[:mid]
        high = arr[mid:]
        mergesort(low)
        mergesort(high)
        
        i=j=k=0
        while i<len(low) and j<len(high):
            if low[i] <= high[j]:
                arr[k] = low[i]
                i+=1
            else:
                arr[k] = high[j]
                j+=1
            k+=1
        
        while i<len(low):
            arr[k] = low[i]
            i+=1
            k+=1
            
        while j<len(high):
            arr[k] = high[j]
            k+=1
            j+=1
    return(arr)
        
arra = [354,2892,12,34,90,22]
mergesort(arra)
