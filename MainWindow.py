from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QSplitter
from ControlPanel import ControlPanel
from GLWidget import GLWidget
from drawing import *


# Главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("0303 Болкунов В. О. Лабораторная работа № 2")
        self.control = ControlPanel(self)
        self.glwidget = GLWidget(self)
        sp = QSplitter(self)
        sp.addWidget(self.glwidget)
        sp.addWidget(self.control)
        sp.setStretchFactor(0, 1)

        self.setCentralWidget(sp)
        self.resize(900, 600)

        # Выбранный примитив
        self.primitive = None
        # Задаём рендер-функцию
        self.glwidget.function = self.renderFunction
        # Обновление ползунков при изменении размеров окна
        self.glwidget.viewPortResized.connect(self.onGLResize)

        c = self.control
        for i in [c.scissorsX, c.scissorsY, c.scissorsH, c.scissorsW, c.scissorsH, c.transparencyRef]:
            i.valueChanged.connect(self.redraw)
        for i in [c.primitiveSelector, c.transparencyFunc, c.sFactor, c.dFactor]:
            i.selectedSignal.connect(self.redraw)

        #
        self.onGLResize(9999, 9999)
        c.scissorsW.setValue(c.scissorsW.maximum())
        c.scissorsH.setValue(c.scissorsH.maximum())

    # Обработка изменения размеров окна
    @QtCore.pyqtSlot(int, int)
    def onGLResize(self, w, h):
        self.control.scissorsW.setMaximum(w)
        self.control.scissorsH.setMaximum(h)
        self.control.scissorsX.setMaximum(w)
        self.control.scissorsY.setMaximum(h)

    def renderFunction(self):
        # Размытие цвета между вершинами
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glLineWidth(10)
        gl.glPointSize(10)

        # Отсечение
        gl.glEnable(gl.GL_SCISSOR_TEST)
        gl.glScissor(
            self.control.scissorsX.value(), self.control.scissorsY.value(),
            self.control.scissorsW.value(), self.control.scissorsH.value()
        )

        # Прозрачность
        gl.glEnable(gl.GL_ALPHA_TEST)
        gl.glAlphaFunc(
            self.control.transparencyFunc.selectedObject,
            self.control.transparencyRef.value() / self.control.transparencyRef.maximum()
        )

        # Смешивание
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(self.control.sFactor.selectedObject, self.control.dFactor.selectedObject)

        # Отрисовка
        renderers[self.control.primitiveSelector.selectedObject]()

    # Вызов обновления изображения
    @QtCore.pyqtSlot()
    def redraw(self):
        self.glwidget.update()
