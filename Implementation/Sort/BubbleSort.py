def bubbleSort(arr):
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            # if arr[i] < arr[j]:
            #     arr[i], arr[j] = arr[j], arr[i]

            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                print(arr)

    return arr
print(bubbleSort([3,7,3,9,0,1,60,23,51,55,84,12]))
