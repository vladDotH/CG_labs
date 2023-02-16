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

        self.setCentralWidget(sp)
        self.resize(800, 600)

        # Словарь количества генерируемых точек в одной фигуре
        self.pointsCount = dict([
            (gl.GL_POINTS, 1),
            (gl.GL_LINES, 2),
            (gl.GL_LINE_STRIP, 2),
            (gl.GL_LINE_LOOP, 2),
            (gl.GL_TRIANGLES, 3),
            (gl.GL_TRIANGLE_STRIP, 3),
            (gl.GL_TRIANGLE_FAN, 3),
            (gl.GL_QUADS, 4),
            (gl.GL_QUAD_STRIP, 4),
            (gl.GL_POLYGON, 1),
        ])

        # Сгенерированные фигуры
        self.objects = []
        # Выбранный примитив
        self.primitive = None
        # Начальная инициализация
        self.primitiveSelected(list(self.pointsCount.keys())[0])

        self.control.primitiveSelector.primitiveSelected.connect(self.primitiveSelected)
        self.control.recreate.clicked.connect(self.regenerate)
        self.control.objectsCount.valueChanged.connect(self.redraw)
        self.control.pointsSize.valueChanged.connect(self.redraw)
        self.control.lineWidth.valueChanged.connect(self.redraw)

    # Установка опций рисования
    @staticmethod
    def setOptions(line: float, points: float):
        # Размытие цвета между вершинами
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glLineWidth(line)
        gl.glPointSize(points)

    # Повторная генерация фигур
    @QtCore.pyqtSlot()
    def regenerate(self):
        self.objects = generateFigures(self.pointsCount[self.primitive], self.control.objectsCount.maximum())
        self.redraw()

    # Генерация фигур при изменении примитива
    @QtCore.pyqtSlot(gl.Constant)
    def primitiveSelected(self, primitive):
        self.primitive = primitive
        self.objects = generateFigures(self.pointsCount[primitive], self.control.objectsCount.maximum())

        # Рендер функция вызывает функцию установки опций и функцию рисования с заданными параметрами
        self.glwidget.function = lambda: [
            self.setOptions(self.control.lineWidth.value(), self.control.pointsSize.value()),
            drawFigures(self.objects[:self.control.objectsCount.value()], self.primitive)
        ]
        self.redraw()

    # Вызов обновления изображения
    @QtCore.pyqtSlot()
    def redraw(self):
        self.glwidget.update()
