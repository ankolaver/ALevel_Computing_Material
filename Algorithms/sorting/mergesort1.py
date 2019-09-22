def mergesort(inputli):
    print("Splitting", inputli)
    if len(inputli) > 1:
        mid = len(inputli)//2
        left = inputli[:mid]
        right = inputli[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0

        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                inputli[k] = left[i]
                i+=1
            else:
                inputli[k] = right[j]
                j+=1
            k+=1
        while i<len(left):
            inputli[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            inputli[k] = right[j]
            j+=1
            k+=1
        print("Merging",inputli)

st = [54,26,93,17,77,31,44,55,20]
mergesort(st)
