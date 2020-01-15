#less pythonic way, recursion and list comprehension
def quickersort(arr):
    if len(arr)>1:
        #arr[0] is the pivot
        return quicksort([i for i in arr[1:] if i < arr[0]])+[arr[0]]+quicksort([i for i in arr[1:] if i > arr[0]])

    else:
        return arr

array = [9,2,4,1,6,3]
print(quickersort(array))
