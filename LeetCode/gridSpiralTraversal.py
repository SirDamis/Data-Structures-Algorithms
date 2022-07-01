def maxtrix_spiral(M):
    if M == []:
        return []
    answer = []

    rowsEnd, rowsBegin = len(M)-1, 0
    columnsEnd, columnsBegin = len(M[0])-1, 0

    while (rowsBegin <= rowsEnd) and (columnsBegin <= columnsEnd):
        # Transverse Right:
        for i in range(columnsBegin, columnsEnd+1):
            answer.append(M[rowsBegin][i])
        rowsBegin += 1
        # Traverse Down
        for i in range(rowsBegin, rowsEnd+1):
            answer.append(M[i][columnsEnd])
        columnsEnd -= 1
        # Traverse Left
        if rowsBegin <= rowsEnd:
            for i in range(columnsEnd, columnsBegin-1, -1):
                answer.append(M[rowsEnd][i])
            rowsEnd -= 1
        # Traverse Up
        if columnsBegin <= columnsEnd:
            for i in range(rowsEnd, rowsBegin-1, -1):
                answer.append(M[i][columnsBegin])
            columnsBegin += 1



        # answer.extend(M[rows-1][columns-1])
        # answer.extend(M[-1][::-1])
        # M.pop()


    return answer

rows = 4
columns = 5

M = [[0 for _ in range(columns)] for _ in range(rows)]
k=1
for i in range(rows):
    for j in range(columns):

        M[i][j] = k
        k+=1
print(M)

print(maxtrix_spiral(M))
