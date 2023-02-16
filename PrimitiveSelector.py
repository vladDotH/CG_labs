from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QComboBox
from OpenGL import GL as gl
from typing import List


class PrimitiveSelector(QComboBox):
    primitiveSelected = QtCore.pyqtSignal(gl.Constant)

    def __init__(self, primitives: List[gl.Constant], parent=None):
        super().__init__(parent)
        self.primitives = primitives
        self.addItems(list(map(lambda p: p.name, primitives)))
        self.currentIndexChanged.connect(self.selected)

    @QtCore.pyqtSlot(int)
    def selected(self, i):
        self.primitiveSelected.emit(self.primitives[i])

