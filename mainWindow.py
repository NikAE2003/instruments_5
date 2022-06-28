from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from calculator import Calculator
from converter import Converter
from simpleTable import SimpleTable
from calculator import Calculator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(700, 600)

        self.initUI()
        self.connections()

    def initUI(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.mainLayout = QGridLayout(self.centralWidget)

        self.formLayout = QFormLayout()
        self.formLayout.setContentsMargins(0,0,0,0)

        self.a_label = QLabel('A', self.centralWidget)

        self.b_label = QLabel('B', self.centralWidget)

        self.a_field = QSpinBox(self.centralWidget)
        self.a_field.setButtonSymbols(QSpinBox.NoButtons)
        self.a_field.setMaximum(1000)

        self.b_field = QSpinBox(self.centralWidget)
        self.b_field.setButtonSymbols(QSpinBox.NoButtons)
        self.b_field.setMaximum(1000)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.a_label)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.a_field)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.b_label)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.b_field)

        self.mainLayout.addLayout(self.formLayout, 0, 0, 1, 2)

        self.mainTable = QTableWidget(self.centralWidget)
        self.mainTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainLayout.addWidget(self.mainTable, 1, 0, 2, 1)

        self.simpleTable = QTableWidget(self.centralWidget)
        self.simpleTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.mainLayout.addWidget(self.simpleTable, 1, 1, 1, 1)

        self.outLayout = QVBoxLayout()
        self.outLayout.setContentsMargins(0,0,0,0)

        self.a_lineEdit = QLineEdit(self.centralWidget)
        self.a_lineEdit.setPlaceholderText('A')
        self.a_lineEdit.setReadOnly(True)
        self.b_lineEdit = QLineEdit(self.centralWidget)
        self.b_lineEdit.setPlaceholderText('B')
        self.b_lineEdit.setReadOnly(True)

        self.outLayout.addWidget(self.a_lineEdit)
        self.outLayout.addWidget(self.b_lineEdit)

        self.mainLayout.addLayout(self.outLayout, 2, 1, 1, 1)

        self.getResult_button = QPushButton('Расчитать', self.centralWidget)
        self.mainLayout.addWidget(self.getResult_button, 3, 0, 1, 1)
        
    def connections(self):
        self.a_field.valueChanged.connect(self.setMainTableRowsCount)
        self.b_field.valueChanged.connect(self.setMainTableColumnsCount)
        self.getResult_button.pressed.connect(self.getResult)
    
    def getResult(self):
        self.converter = Converter(self.mainTable)
        self.simpleTable_handler = SimpleTable(self.simpleTable)
        self.calculator = Calculator()
        self.converter.comunicator.send.connect(self.simpleTable_handler.fillTable)
        self.converter.comunicator.send.connect(self.calculator.calculate)
        self.converter.convert()

        self.a_lineEdit.setText(self.calculator.a)
        self.b_lineEdit.setText(self.calculator.b)

    def setMainTableRowsCount(self, value):
        self.mainTable.setRowCount(value)
        self.mainTable.setVerticalHeaderLabels([f'A{i+1}' for i in range(value)])
    
    def setMainTableColumnsCount(self, value):
        self.mainTable.setColumnCount(value)
        self.mainTable.setHorizontalHeaderLabels([f'B{i+1}' for i in range(value)])