from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QSplitter
from ControlPanel import ControlPanel
from GLWidget import GLWidget
from drawing import *


# Главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("0303 Болкунов В. О. Лабораторная работа № 1")
        self.control = ControlPanel(self)
        self.glwidget = GLWidget(self)
        sp = QSplitter(self)
        sp.addWidget(self.glwidget)
        sp.addWidget(self.control)
        sp.setStretchFactor(0, 1)

        self.control.primitiveSelector.primitiveSelected.connect(self.primitiveSelected)
        self.control.recreate.clicked.connect(self.recreate)
        self.setCentralWidget(sp)
        self.resize(800, 600)

        # Словарь рендер-функции в соответствии с константами примитивов
        self.drawers = dict([
            (gl.GL_POINT, drawPoints),
            (gl.GL_LINES, drawLines),
            (gl.GL_LINE_STRIP, drawLinesStrip),
            (gl.GL_LINE_LOOP, drawLinesLoop),
            (gl.GL_TRIANGLES, drawTriangles),
            (gl.GL_TRIANGLE_STRIP, drawTrianglesStrip),
            (gl.GL_TRIANGLE_FAN, drawTrianglesFan),
            (gl.GL_QUADS, drawQuads),
            (gl.GL_QUAD_STRIP, drawQuadsStrip),
            (gl.GL_POLYGON, drawPolygon),
        ])
        self.primitiveSelected(list(self.drawers.keys())[0])

    @QtCore.pyqtSlot(gl.Constant)
    def primitiveSelected(self, primitive):
        self.glwidget.function = self.drawers[primitive]
        self.glwidget.update()

    @QtCore.pyqtSlot()
    def recreate(self):
        self.glwidget.update()
