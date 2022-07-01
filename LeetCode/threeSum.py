def maxProduct(nums):
    firstmax = 0
    secondmax = 0

    for value in nums:
        if value >= secondmax:
            firstmax = secondmax
            secondmax = value
        else:
            firstmax = max(value, firstmax)

        print(firstmax, secondmax)
    return (secondmax - 1) * (firstmax - 1)
nums = [10,2,5,2]
print(maxProduct(nums))
