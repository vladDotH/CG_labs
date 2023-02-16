from OpenGL import GL as gl
import random


def randomPoint(min=-1, max=1):
    return [random.uniform(min, max) for i in range(2)]


def randomColor():
    return [random.uniform(-1, 1) for i in range(3)]


# Генерация m фигур каждая из n точек
def generateFigures(n, m):
    return list(list(randomPoint() for i in range(n)) for i in range(m))


# Рисование фигур со случайным цветом
def drawFigures(figures, type):
    gl.glBegin(type)
    for points in figures:
        gl.glColor3dv(randomColor())
        for p in points:
            gl.glVertex2dv(p)
    gl.glEnd()
