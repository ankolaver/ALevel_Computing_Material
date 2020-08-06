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
    return arr
  
#main
arr = [12, 11, 13, 5, 6] 
insertionSort(arr) 

def insertionsort(arr):
    for i in range(len(arr)):
        insert_val = arr[i]
        insert_index = i
        while insert_index > 0 and arr[insert_index-1] > insert_val:
            arr[insert_index] = arr[insert_index-1]
            insert_index-=1
        arr[insert_index] = insert_val

    return arr

insertionsort([9,6,2,4,1,8])
