'''Bubble sort has a worst-case and average complexity
of О(n2), where n is the number of items being sorted.
Most practical sorting algorithms have substantially
better worst-case or average complexity, often O(n log n).
The function below always runs O(n^2) time even if the array is sorted.
It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.'''

def bubblesort(arr):
    lenarr = len(arr)

    for i in range(lenarr):
        swapmulti = False
        for k in range(0, lenarr-i-1):
            if arr[k]>arr[k+1]:
                arr[k],arr[k+1] = arr[k+1], arr[k]
                swapmulti = True
                #do not need to go through loop again (efficient)

        if swapmulti == False:
            break
    print(arr1)

arr1 = [12,2,34,29,4,6,6,7]
bubblesort(arr1)
