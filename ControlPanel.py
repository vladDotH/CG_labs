from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from OpenGL import GL as gl

from PrimitiveSelector import PrimitiveSelector


# Виджет панели управления
class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lt = QVBoxLayout(self)
        self.setLayout(lt)
        self.primitiveSelector = PrimitiveSelector([
            gl.GL_POINT, gl.GL_LINES, gl.GL_LINE_STRIP, gl.GL_LINE_LOOP, gl.GL_TRIANGLES,
            gl.GL_TRIANGLE_STRIP, gl.GL_TRIANGLE_FAN, gl.GL_QUADS, gl.GL_QUAD_STRIP, gl.GL_POLYGON
        ], self)
        self.recreate = QPushButton("Пересоздать объект", self)
        lt.addWidget(self.primitiveSelector)
        lt.addWidget(self.recreate)
