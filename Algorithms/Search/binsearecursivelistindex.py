def binarysearch(arr, target):
    mid = len(arr)//2
    if target==arr[mid]:
        print(arr[mid])

    elif len(arr)==1:
        print("Cannot find")
        return False
    
    elif target>arr[mid]:
        return binarysearch(arr[mid:], target)

    elif target<arr[mid]:
        return binarysearch(arr[:mid], target)

    return arr 
array1 = [1,2,3,4,5,6,7,8,9,10]
binarysearch(array1,12)
binarysearch(array1,3)
