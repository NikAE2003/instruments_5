def getIndexes(matrix:list):
        rows = []
        for i, row in enumerate(matrix):
            for elem in row:
                if elem != 0: 
                    rows.append(i)
                    break

        columns = []
        for j, elem in enumerate(matrix[rows[0]]):
            if elem != 0: columns.append(j)

        return rows, columns