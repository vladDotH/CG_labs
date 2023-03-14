from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow, QSplitter
from ControlPanel import ControlPanel
from GLWidget import GLWidget
from drawing import *


# Главное окно
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("0303 Болкунов В. О. Лабораторная работа № 3")
        self.control = ControlPanel(self)
        self.glwidget = GLWidget(self)
        sp = QSplitter(self)
        sp.addWidget(self.glwidget)
        sp.addWidget(self.control)
        sp.setStretchFactor(0, 1)

        self.setCentralWidget(sp)
        self.resize(900, 600)

        # Задаём рендер-функцию
        self.glwidget.function = self.renderFunction

        self.radiusFraction = 1000

        self.control.radius.setMaximum(self.radiusFraction)
        self.control.iterations.setMaximum(50)
        self.control.iterations.setTickInterval(1)
        self.control.radius.valueChanged.connect(self.redraw)
        self.control.iterations.valueChanged.connect(self.redraw)

    def renderFunction(self):
        radius = self.control.radius.value() / self.radiusFraction
        # Размытие цвета между вершинами
        gl.glShadeModel(gl.GL_SMOOTH)
        # Ширина линий
        gl.glLineWidth(1 + 15 * radius)
        # Генерация шестиугольников
        dots = generate(self.control.iterations.value(), radius)
        # Рисование их линий
        drawLines(dots)
        # Рисование окружностей в вершинах шестиугольников
        for i in range(len(dots)):
            for p in range(len(dots[i])):
                drawCircle(radius / 2, dots[i][p], colors[(i + p) % 4])

    # Вызов обновления изображения
    @QtCore.pyqtSlot()
    def redraw(self):
        self.glwidget.update()
