def binarySearch(arr, target):
    a, b = 0, len(arr)-1
    while a < b:
        k = (a+b) // 2
        print(a, b, k)
        if arr[k] == target:
            return 'Found'
        if arr[k] > target:
            b = k-1
        else:
            a = k+1
    return 'Not Found'

print(binarySearch([1,2,3,4,5,6,7,8], 6))
