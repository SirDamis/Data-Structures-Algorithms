"""
Daily Coding Problem - Day 36

Given an array of strictly characters 'R', 'G' and 'B', segregate the values of the array so that all the
Rs come first and the Gs come second and the Bs come last

Do this in linear time and in place
"""
def solution(colorArray):
    colorMap = {}
    for color in colorArray:
        colorMap[color] = colorMap.get(color, 0) + 1
    for idx in range(len(colorArray)):
        if colorMap['R']:
            colorMap['R'] -= 1
            colorArray[idx] = 'R'
        elif colorMap['G']:
            colorMap['G'] -= 1
            colorArray[idx] = 'G'
        elif colorMap['B']:
            colorMap['B'] -= 1
            colorArray[idx] = 'B'
    return  colorArray
print(solution(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
