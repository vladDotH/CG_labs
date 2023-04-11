from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel
from PyQt6 import QtCore


# Виджет панели управления
class ControlPanel(QWidget):
    weightsChanged = QtCore.pyqtSignal()

    def __init__(self, weights, parent=None):
        super().__init__(parent)
        lt = QVBoxLayout(self)
        self.setLayout(lt)

        weightsLabel = QLabel('Веса NURBS сплайна', self)
        wLabels = [QLabel(f'W{i}') for i in range(weights)]
        self.wSliders = [QSlider(Qt.Orientation.Horizontal) for i in range(weights)]

        for w in [weightsLabel]:
            lt.addWidget(w)

        for i in range(weights):
            lt.addWidget(wLabels[i])
            lt.addWidget(self.wSliders[i])
            self.wSliders[i].valueChanged.connect(lambda: self.weightsChanged.emit())
            self.wSliders[i].setMaximum(100)
            self.wSliders[i].setMinimum(1)

        lt.addStretch()
