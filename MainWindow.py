from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QSplitter
from ControlPanel import ControlPanel
from GLWidget import GLWidget
from drawing import *
from OpenGL import GL as gl


# Главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Создаём виджет OpenGL
        self.glwidget = GLWidget(self)

        # Задаём рендер-функцию
        self.glwidget.function = self.renderFunction

        # Точки окружности
        self.P = P = [
            np.array([0.9, 0]),
            np.array([0.9, 0.9]),
            np.array([0, 0.9]),
            np.array([-0.9, 0.9]),
            np.array([-0.9, 0]),
            np.array([-0.9, -0.9]),
            np.array([0, -0.9]),
            np.array([0.9, -0.9]),
            np.array([0.9, 0]),
        ]

        # Виджет управления
        self.control = ControlPanel(len(self.P), self)

        # Задаём начальные веса
        for i in range(9):
            if i % 2 == 0:
                self.control.wSliders[i].setValue(60)
            else:
                self.control.wSliders[i].setValue(int(60 / (2 ** (1 / 2))))

        # Задаём узловой вектор
        self.T = np.array([
            0, 0, 0,
            np.pi / 2, np.pi / 2,
            np.pi, np.pi,
            3 * np.pi / 2, 3 * np.pi / 2,
            np.pi * 2, np.pi * 2, np.pi * 2
        ]) / (2 * np.pi)

        self.onWeightsChanged()
        self.control.weightsChanged.connect(self.onWeightsChanged)

        sp = QSplitter(self)
        sp.addWidget(self.glwidget)
        sp.addWidget(self.control)
        sp.setStretchFactor(0, 1)
        self.setCentralWidget(sp)
        self.resize(800, 600)
        self.setWindowTitle("0303 Болкунов В. О. Лабораторная работа №4")

    def onWeightsChanged(self):
        self.W = [s.value() for s in self.control.wSliders]
        self.rebuildSpline()

    # Сборка сплайна
    def rebuildSpline(self):
        self.F, N = buildNurbs(self.T, self.P, self.W)
        X = np.linspace(0, 1, 100)
        self.Points = [self.F(x) for x in X]
        self.redraw()

    def renderFunction(self):
        gl.glPointSize(10)
        gl.glLineWidth(5)
        gl.glBegin(gl.GL_LINE_STRIP)
        gl.glColor3dv((0, 0, 0))
        for p in self.Points:
            gl.glVertex2dv(p)
        gl.glEnd()
        gl.glBegin(gl.GL_POINTS)
        gl.glColor3dv((1, 0, 0))
        for p in self.P:
            gl.glVertex2dv(p)
        gl.glEnd()

    # Вызов обновления изображения
    @QtCore.pyqtSlot()
    def redraw(self):
        self.glwidget.update()
