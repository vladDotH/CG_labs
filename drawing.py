from typing import Callable
from OpenGL import GL as gl
import random


def randomPoint(min=-1, max=1):
    return [random.uniform(min, max) for i in range(2)]


def randomColor():
    return [random.uniform(-1, 1) for i in range(3)]


POINTS = 10


def drawPoints():
    gl.glBegin(gl.GL_POINTS)
    for i in range(POINTS):
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(randomPoint())
    gl.glEnd()


LINES = 5


def drawLines(type=gl.GL_LINES):
    gl.glBegin(type)
    for i in range(LINES):
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(randomPoint())
        gl.glVertex2dv(randomPoint())
    gl.glEnd()


def drawLinesStrip():
    drawLines(gl.GL_LINE_STRIP)


def drawLinesLoop():
    drawLines(gl.GL_LINE_LOOP)


TRIANGLES = 5


def drawTriangles(type=gl.GL_TRIANGLES):
    gl.glBegin(type)
    for i in range(TRIANGLES):
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(randomPoint())
        gl.glVertex2dv(randomPoint())
        gl.glVertex2dv(randomPoint())
    gl.glEnd()


def drawTrianglesStrip():
    drawTriangles(gl.GL_TRIANGLE_STRIP)


def drawTrianglesFan():
    drawTriangles(gl.GL_TRIANGLE_FAN)


QUADS = 4


def drawQuads(type=gl.GL_QUADS):
    gl.glBegin(type)
    for i in range(QUADS):
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(randomPoint())
        gl.glVertex2dv(randomPoint())
        gl.glVertex2dv(randomPoint())
        gl.glVertex2dv(randomPoint())
    gl.glEnd()


def drawQuadsStrip():
    drawQuads(gl.GL_QUAD_STRIP)


POLYGON_VERTICES = 8


def drawPolygon():
    gl.glBegin(gl.GL_POLYGON)
    for i in range(POLYGON_VERTICES):
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(randomPoint())
    gl.glEnd()
