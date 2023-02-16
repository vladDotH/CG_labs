from OpenGL import GL as gl
from PyQt6.QtOpenGLWidgets import QOpenGLWidget


class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = (0, 1, 0)

    def initializeGL(self):
        gl.glClearColor(1, 1, 1, 1)

    def paintGL(self):
        gl.glLineWidth(50.0)
        gl.glPointSize(10)
        gl.glColor3f(*self.color)
        gl.glBegin(gl.GL_POINTS)
        gl.glVertex2f(0, 0)
        gl.glVertex2f(0, 1)
        gl.glVertex2f(1, 0)
        gl.glVertex2f(1, 1)
        gl.glVertex2f(0, -1)
        gl.glVertex2f(-1, 0)
        gl.glVertex2f(-1, -1)
        gl.glVertex2f(-1, 1)
        gl.glVertex2f(1, -1)
        gl.glEnd()
