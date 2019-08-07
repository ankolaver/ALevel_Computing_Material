def bubblesort(arr):
    lenarr = len(arr)

    for i in range(lenarr):
        swapmulti = False
        for k in range(0, lenarr-i-1):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1] = arr[k+1], arr[k]
                swapmulti = True

        if swapmulti == False:
            break

        toprint = []
        for i in range(len(arr1)):
            toprint.append(i)
    print(arr1)

arr1 = [12,2,34,29,4,6,6,7]
bubblesort(arr1)
