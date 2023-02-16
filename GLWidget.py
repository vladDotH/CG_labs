from OpenGL import GL as gl
from PyQt6.QtOpenGLWidgets import QOpenGLWidget


class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.function = None

    def initializeGL(self):
        gl.glClearColor(1, 1, 1, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    def paintGL(self):
        gl.glShadeModel(gl.GL_SMOOTH)
        gl.glLineWidth(10.0)
        gl.glPointSize(10)
        if self.function is not None:
            self.function()



