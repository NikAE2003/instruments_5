from PyQt5.QtWidgets import QTableWidget, QWidget
from PyQt5.QtCore import pyqtSignal, QObject

class Comunicator(QObject):
    send = pyqtSignal(list)

class Converter():
    def __init__(self, table:QTableWidget):
        self._table = table
        self._rowCount = self._table.rowCount()
        self._columnCount = self._table.columnCount()
        self.comunicator = Comunicator()

    def convert(self):
        self._matrix = [[int(self._table.item(i,j).text()) for i in range(self._columnCount)] for j in range(self._rowCount)]
        self.calculateSimple()

    def calculateSimple(self):
        while (self._rowCount > 2 and self._columnCount > 2):
            self.deleteRows()
            self.deleteColumns()

        self.comunicator.send.emit(self._matrix)
    
    def deleteRows(self):
        isStoped = False
        for i in range(self._rowCount):
            for j in range(self._rowCount):
                if i == j: continue

                if checkRow(i, j, self._matrix):
                    setZeroRow(i, self._matrix)
                    self._rowCount -= 1
                    isStoped = True
                    break
            if isStoped:
                break

    def deleteColumns(self):
        isStoped = False
        for i in range(self._columnCount):
            for j in range(self._columnCount):
                if i == j: continue

                if checkColumn(i, j, self._matrix):
                    setZeroColumn(i, self._matrix)
                    self._columnCount -= 1
                    isStoped = True
                    break
            if isStoped:
                break

def checkRow(i, j, matrix):
    if (isZeroRow(i, matrix) or isZeroRow(j, matrix)): return False

    for first, second in zip(matrix[i], matrix[j]):
        if first > second: return False
    
    return True

def isZeroRow(i, matrix):
    for value in matrix[i]:
        if value != 0: return False

    return True

def setZeroRow(i, matrix):
    for j in range(len(matrix[i])):
        matrix[i][j] = 0

def checkColumn(i, j, matrix):
    if (isZeroColumn(i, matrix) or isZeroColumn(j, matrix)): return False

    for k in range(len(matrix)):
        if matrix[k][i] > matrix[k][j]: return False
    
    return True

def isZeroColumn(i, matrix):
    for j in range(len(matrix)):
        if matrix[j][i] != 0: return False

    return True

def setZeroColumn(i, matrix):
    for j in range(len(matrix)):
        matrix[j][i] = 0