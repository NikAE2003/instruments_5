from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from matrixFuncs import getIndexes

class SimpleTable():
    def __init__(self, table:QTableWidget):
        self._table = table
    
    def fillTable(self, matrix):
        rows, columns = getIndexes(matrix)
        self._table.setRowCount(len(columns))
        self._table.setColumnCount(len(rows))
        self._table.setVerticalHeaderLabels([f'A{i+1}' for i in rows])
        self._table.setHorizontalHeaderLabels([f'B{i+1}' for i in columns])

        for i, spidy in enumerate(rows):
            for j, mj in enumerate(columns):
                self._table.setItem(i, j, QTableWidgetItem(str(matrix[spidy][mj])))


    