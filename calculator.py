from matrixFuncs import getIndexes

class Calculator():
    def calculate(self, matrix):
        self._matrix = matrix

        values = []
        for row in self._matrix:
            for elem in row:
                if elem != 0:
                    values.append(elem)

        rows, columns = getIndexes(self._matrix)
        
        _x1 = (values[3] - values[1])/(values[0] - values[1] + values[3] - values[2])
        _x2 = 1 - _x1 
        _v = values[0] * _x1 + values[1] * _x2

        values = ['0.0' for i in range(len(matrix))]
        values[rows[0]] = str(_x1)
        values[rows[1]] = str(_x2)

        self.a = f'A: ({"; ".join(values)}), {str(_v)}'

        values = ['0.0' for i in range(len(matrix[0]))]
        values[columns[0]] = str(_x1)
        values[columns[1]] = str(_x2)

        self.b = f'B: ({"; ".join(values)}), {str(_v)}'