def insertion(arr):
    
    for k in range(1,len(arr)):
        temp = k
        while temp>0 and arr[temp-1]>arr[temp]:
            arr[temp-1],arr[temp] = arr[temp],arr[temp-1]
            temp-=1
    print(arr)

array = [3,9,12,1,2,4]
insertion(array)


#correct copy
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
#main
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 
