from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSlider, QLabel
from OpenGL import GL as gl

from PrimitiveSelector import PrimitiveSelector


# Виджет панели управления
class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lt = QVBoxLayout(self)
        self.setLayout(lt)
        self.primitiveSelector = PrimitiveSelector([
            gl.GL_POINTS, gl.GL_LINES, gl.GL_LINE_STRIP, gl.GL_LINE_LOOP, gl.GL_TRIANGLES,
            gl.GL_TRIANGLE_STRIP, gl.GL_TRIANGLE_FAN, gl.GL_QUADS, gl.GL_QUAD_STRIP, gl.GL_POLYGON
        ], self)
        self.recreate = QPushButton("Пересоздать объект", self)

        pointsLabel = QLabel('Размер точек', self)
        self.pointsSize = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.pointsSize.setMinimum(1)
        self.pointsSize.setMaximum(100)
        self.pointsSize.setValue(10)

        linesLabel = QLabel('Размер линий', self)
        self.lineWidth = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.lineWidth.setMinimum(1)
        self.lineWidth.setMaximum(10)
        self.lineWidth.setValue(5)

        countLabel = QLabel('Количество объектов', self)
        self.objectsCount = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        self.objectsCount.setMinimum(1)
        self.objectsCount.setMaximum(20)
        self.objectsCount.setValue(5)

        for i in [
            self.primitiveSelector, self.recreate, pointsLabel, self.pointsSize,
            linesLabel, self.lineWidth, countLabel, self.objectsCount
        ]:
            lt.addWidget(i)

        lt.addStretch()
