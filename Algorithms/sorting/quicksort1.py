#pivot sort
def quiksort(arr):
    less = []
    more = []
    equal = []

    if len(arr)>1:
        pivot = arr[0]
        for j in arr:
            if j<pivot:
                less.append(j)
            elif j>pivot:
                more.append(j)
            else:
                equal.append(j)
        return sort(less)+equal+sort(more) 
    else:
        return arr
  
arra = [23,5,1,9,2,7,15]
quiksort(arra)
