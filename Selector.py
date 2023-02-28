from typing import List

from PyQt6 import QtCore
from PyQt6.QtWidgets import QComboBox
from OpenGL import GL as gl


# Виджет выбора констант
class Selector(QComboBox):
    primitiveSelected = QtCore.pyqtSignal(gl.Constant)

    def __init__(self, objects: List[gl.Constant], parent=None):
        super().__init__(parent)
        self.objects = objects
        self.addItems(list(map(lambda p: p.name, objects)))
        self.currentIndexChanged.connect(self.selected)

    @QtCore.pyqtSlot(int)
    def selected(self, i):
        self.primitiveSelected.emit(self.objects[i])
