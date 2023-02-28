from typing import List

from PyQt6 import QtCore
from PyQt6.QtWidgets import QComboBox
from OpenGL import GL as gl


# Виджет выбора констант
class Selector(QComboBox):
    selectedSignal = QtCore.pyqtSignal(gl.Constant)

    def __init__(self, objects: List[gl.Constant], parent=None):
        super().__init__(parent)
        self.objects = objects
        self.selectedObject = objects[0]
        self.addItems(list(map(lambda p: p.name, objects)))
        self.currentIndexChanged.connect(self.onSelected)

    @QtCore.pyqtSlot(int)
    def onSelected(self, i):
        self.selectedObject = self.objects[i]
        self.selectedSignal.emit(self.selectedObject)
