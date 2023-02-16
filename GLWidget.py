from OpenGL import GL as gl
from PyQt6.QtOpenGLWidgets import QOpenGLWidget


# Виджет OpenGL
class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Функция вызываемая в цикле отрисовки (при обновлениях)
        self.function = None

    # Функция вызываемая перед любым обновлением
    def initializeGL(self):
        # Заливка кадра
        gl.glClearColor(1, 1, 1, 1)
        # Очистка буферов (цвета и глубины)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    # Функция вызываемая при обновлении (посредством update или при изменении размеров)
    def paintGL(self):
        # Размытие цвета
        gl.glShadeModel(gl.GL_SMOOTH)
        # Ширина линии
        gl.glLineWidth(10.0)
        # Размер точек
        gl.glPointSize(10)
        # Вызов рендер-функции
        if self.function is not None:
            self.function()
