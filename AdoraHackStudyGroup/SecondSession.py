"""
Develop an algorithm to find the shortest distance between two points in M X N 2D plane, bearing in mind that random
points in the plane may have obstacle

[-,-,-,-,-,-,-,-,-,-]
[-,-,A,-,-,-,-,-,-,-]
[-,-,-,-,-,-,-,-,-,-]
[-,-,-,-,X,-,-,-,-,-]
[-,-,-,-,-,-,-,-,B,-]
[-,-,-,-,-,-,-,-,-,-]
[-,-,-,-,-,-,X,-,-,-]

pointA = r1, c1
pointB = r2, c2

Transversing right = r1, c1 -> r1, c1+1
Transversing left = r1, c1 -> r1, c1-1
Transversing up = r1, c1 -> r1-1, c1
Transversing down = r1, c1 -> r1+1, c1

Things to note
    - Endless loop
    - Encounter with obstacles
    - Out of bound / Overflow

    [A, -, -]
    [-, X, -]
    [-, -, B]

                        [0,0]
           /        /         /      \
        [-1,0] X, [1,0] OK, [0,1] OK, [0, -1] X
                    /
            [0,0] X, [2,0]OK, [1,-1]X, [1,1] X



    Test Plane:
        [0,0,0,0]
        [0,0,-1,0]
        [0,-1,0,0]
        [0,0,0,0]
    point A = 1,1
    point B = 2,3
    Shortest Path = 5
"""
from collections import deque

def shortestDistance(plane, r1, c1, r2, c2, current_dist=0):
    if r1 == r2 and c1 == c2:
        return 1
    # Out of bound check
    if r1 < 0 or r1 >= len(plane) or c1 < 0 or c1 >= len(plane[0]):
        return (len(plane) * len(plane[0])) + 1
    # Obstacles  or Visited Check
    if plane[r1][c1] == -1 or plane[r1][c1] == 1:
        return (len(plane) * len(plane[0])) + 1
        return -1

    # Visited to 1
    plane[r1][c1] = 1
    current_dist = 1
    # Left Movement
    dist = shortestDistance(plane, r1, c1+1, r2, c2)
    # Right Movement
    dist = min(dist, shortestDistance(plane, r1, c1 - 1, r2, c2))
    # Up Movement
    dist = min(dist, shortestDistance(plane, r1-1, c1, r2, c2))
    # Down Movement
    dist = min(dist, shortestDistance(plane, r1+1, c1, r2, c2))
    plane[r1][c1] = 0
    return current_dist + dist

def findDistance(plane, r1, c1, r2, c2):

    if r1 == r2 and c1 == c2:
        return 0
    return shortestDistance(plane, r1, c1, r2, c2) - 1







class Node:
    def __init__(self, row, col, dist, planeAtNode):
        self.row = row
        self.col = col
        self.dist = dist
        self.planeAtNode = planeAtNode

def isIllegalPos(plane, r, c):
    # Row out of bound
    if r < 0 or r >= len(plane):
        return True
    # Column out of bound
    if c < 0 or c >= len(plane[0]):
        return True
    # Obstacle or Visited
    if plane[r][c] != 0:
        return True
    return False


def bfsShortestDistance(plane, r1, c1, r2, c2):
    dq = deque()
    dq.append(Node(r1, c1, 0, plane.copy()))

    while dq:
        curr = dq.popleft()
        if isIllegalPos(curr.planeAtNode, curr.row, curr.col):
            continue
        # If position found, return
        # First position  will be the shortest distance
        if curr.row == r2 and curr.col == c2:
            return curr.dist
        dq.append(Node(curr.row-1, curr.col, curr.dist+1, plane.copy()))
        dq.append(Node(curr.row+1, curr.col, curr.dist + 1, plane.copy()))
        dq.append(Node(curr.row, curr.col - 1, curr.dist + 1, plane.copy()))
        dq.append(Node(curr.row, curr.col + 1, curr.dist + 1, plane.copy()))
    return -1


def main():
    plane = [
        [0, 0, 0, 0],
        [0, 0, -1, 0],
        [0, -1, 0, 0],
        [0, 0, 0, 0]
    ]
    r1, c1 = 1, 1
    r2, c2 = 2, 3
    distance = findDistance(plane, r1, c1, r2, c2)
    # distance = bfsShortestDistance(plane, r1, c1, r2, c2)
    print(distance)

if __name__ == '__main__':
    main()
