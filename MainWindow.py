from OpenGL import GL as gl
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QHBoxLayout, QSplitter, QVBoxLayout, QSizePolicy

from ControlPanel import ControlPanel
from GLWidget import GLWidget
from PrimitiveSelector import PrimitiveSelector


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("0303 Болкунов В. О. Лабораторная работа № 1")
        self.control = ControlPanel(self)
        self.glwidget = GLWidget(self)
        sp = QSplitter(self)
        sp.addWidget(self.glwidget)
        sp.addWidget(self.control)
        sp.setStretchFactor(1, 1)
        sp.setStretchFactor(2, 4)

        self.control.primitiveSelector.primitiveSelected.connect(self.primitiveSelected)
        self.setCentralWidget(sp)
        self.resize(800, 600)

    @QtCore.pyqtSlot(gl.Constant)
    def primitiveSelected(self, primitive):
        print(primitive)
        self.glwidget.color = (1, 0, 0)
        self.glwidget.update()
