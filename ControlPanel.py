from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel, QGroupBox
from OpenGL import GL as gl

from Selector import Selector


# Виджет панели управления
class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lt = QVBoxLayout(self)
        self.setLayout(lt)

        primitivesLabel = QLabel("Выбор Примитива", self)
        self.primitiveSelector = Selector([
            gl.GL_POINTS, gl.GL_LINES, gl.GL_LINE_STRIP, gl.GL_LINE_LOOP, gl.GL_TRIANGLES,
            gl.GL_TRIANGLE_STRIP, gl.GL_TRIANGLE_FAN, gl.GL_QUADS, gl.GL_QUAD_STRIP, gl.GL_POLYGON
        ], self)

        # Группа отсечения
        scissorsBox = QGroupBox("Тест отсечения", self)
        scissorsLt = QVBoxLayout()
        scissorsBox.setLayout(scissorsLt)
        sxLabel = QLabel('x', self)
        self.scissorsX = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        syLabel = QLabel('y', self)
        self.scissorsY = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        swLabel = QLabel('Ширина w', self)
        self.scissorsW = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        shLabel = QLabel('Высота h', self)
        self.scissorsH = QSlider(QtCore.Qt.Orientation.Horizontal, self)
        for i in [sxLabel, self.scissorsX, syLabel, self.scissorsY, swLabel, self.scissorsW, shLabel, self.scissorsH]:
            scissorsLt.addWidget(i)

        # Группа Прозрачности
        transparencyBox = QGroupBox("Тест прозрачности", self)
        transparencyLt = QVBoxLayout()
        transparencyBox.setLayout(transparencyLt)
        transparencyFuncLabel = QLabel('Функция тестирования')
        self.transparencyFunc = Selector([
            gl.GL_NEVER, gl.GL_LESS, gl.GL_EQUAL, gl.GL_LEQUAL,
            gl.GL_GREATER, gl.GL_NOTEQUAL, gl.GL_GEQUAL, gl.GL_ALWAYS
        ], self)

        transparencyRefLabel = QLabel('Сравниваемое значние')
        self.transparencyRef = QSlider(QtCore.Qt.Orientation.Horizontal, self)

        for i in [transparencyFuncLabel, self.transparencyFunc, transparencyRefLabel, self.transparencyRef]:
            transparencyLt.addWidget(i)

        # Группа Смешивания
        mixBox = QGroupBox("Тест смешивания", self)
        mixLt = QVBoxLayout()
        mixBox.setLayout(mixLt)
        sFactorLabel = QLabel('Входящий фактор')
        self.sFactor = Selector([
            gl.GL_ZERO, gl.GL_ONE, gl.GL_DST_COLOR, gl.GL_ONE_MINUS_DST_COLOR, gl.GL_SRC_ALPHA,
            gl.GL_ONE_MINUS_SRC_ALPHA, gl.GL_DST_ALPHA, gl.GL_ONE_MINUS_DST_ALPHA, gl.GL_SRC_ALPHA_SATURATE
        ], self)

        dFactorLabel = QLabel('dfactor (находящиеся в буфере кадра)')
        self.dFactor = Selector([
            gl.GL_ZERO, gl.GL_ONE, gl.GL_SRC_COLOR, gl.GL_ONE_MINUS_SRC_COLOR, gl.GL_SRC_ALPHA,
            gl.GL_ONE_MINUS_SRC_ALPHA, gl.GL_DST_ALPHA, gl.GL_ONE_MINUS_DST_ALPHA
        ], self)

        for i in [sFactorLabel, self.sFactor, dFactorLabel, self.dFactor]:
            mixLt.addWidget(i)

        #
        for i in [
            primitivesLabel,
            self.primitiveSelector,
            scissorsBox,
            transparencyBox,
            mixBox
        ]:
            lt.addWidget(i)

        lt.addStretch()
