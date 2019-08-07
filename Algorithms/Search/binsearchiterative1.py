def binarysearch(arr,target):
    lower = 0
    upper = len(arr)-1
    found = False
    while lower<=upper and not found:
        mid = (lower+upper)//2
        
        if arr[mid] == target:
            found == True
            print("found the number!")
            return found
            
        else:
            if target<arr[mid]:
                upper = mid-1
            else:
                lower = mid+1
    
    print("Cant find")

array1 = [1,2,3,4,5,6,7,8,9,10]
binarysearch(array1,12)
binarysearch(array1,3)
