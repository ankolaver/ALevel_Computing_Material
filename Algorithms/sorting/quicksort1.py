def quiksort(arr):
    less = []
    more = []
    equal = []

    if len(arr)>1:
        pivot = arr[0]
        for k in arr:
            if k<pivot:
                less.append(k)
            elif k==pivot:
                equal.append(k)
            elif k>pivot:
                more.append(k)
        return quiksort(less)+equal+quiksort(more)
    else:
        return arr
arra = [0,5,1,9,2,7,15]
#quiksort(arra)
print(quiksort(arra))
