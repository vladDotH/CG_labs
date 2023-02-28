from typing import Callable

from OpenGL import GL as gl
import random


def randomColor():
    return [random.uniform(-1, 1) for i in range(3)]


def drawPoints():
    gl.glBegin(gl.GL_POINTS)
    points = [
        (0, 0), (0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1), (0.5, 0.5)
    ]
    for i in points:
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(i)
    gl.glEnd()


def drawLines():
    gl.glBegin(gl.GL_LINES)
    lines = [
        ((-0.5, 0), (0, 1)),
        ((1, 0), (-1, 0.5)),
        ((0.7, -1), (1, 1)),
        ((-0.5, -0.7), (0.8, 0.5)),
        ((-0.4, -0.7), (0.8, -0.5))
    ]
    for i in lines:
        for p in i:
            gl.glColor3dv(randomColor())
            gl.glVertex2dv(p)
    gl.glEnd()


def drawLineStrip():
    gl.glBegin(gl.GL_LINE_STRIP)
    ponts = [
        (-0.5, 0), (-0.7, 0.8),
        (0, 0.6), (1, 0.5),
        (0.7, 0.8), (0.9, -0.8),
        (-0.1, -0.7), (0, 0.95)
    ]
    for p in ponts:
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(p)
    gl.glEnd()


def drawLineLoop():
    gl.glBegin(gl.GL_LINE_LOOP)
    ponts = [
        (-0.5, 0), (-0.7, 0.8),
        (0, 0.6), (1, 0.5),
        (0.7, 0.8), (0.9, -0.8),
        (-0.1, -0.7), (0, 0.95)
    ]
    for p in ponts:
        gl.glColor3dv(randomColor())
        gl.glVertex2dv(p)
    gl.glEnd()


def drawTriangles():
    gl.glBegin(gl.GL_TRIANGLES)
    triangles = [
        ((-0.9, -0.5), (0.4, 0.4), (-0.2, -0.9)),
        ((0.9, -0.5), (-0.4, 0.4), (0.2, -0.9)),
        ((-0.4, 0.9), (0.4, 0.9), (0, -0.4)),
    ]
    colors = [(0.9, 0.2, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5), (0.1, 0.2, 0.8, 0.5)]
    for i, color in zip(triangles, colors):
        gl.glColor4dv(color)
        for p in i:
            gl.glVertex2dv(p)
    gl.glEnd()


def drawTriangleStrip():
    gl.glBegin(gl.GL_TRIANGLE_STRIP)
    points = [
        (-0.9, -0.5), (-0.3, 0.6), (-0.2, -0.9),
        (0.1, -0.1), (0.7, -0.8), (0.8, 0.8), (-0.9, -0.3)
    ]
    colors = [
        (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5),
        (0.2, 0.7, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5), (0.1, 0.2, 0.8, 0.5), (0.1, 0.2, 0.8, 0.5)
    ]
    for i, color in zip(points, colors):
        gl.glColor4dv(color)
        gl.glVertex2dv(i)
    gl.glEnd()


def drawTriangleFan():
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    points = [
        (0, 0), (-0.7, -0.8), (0, -0.9), (0.3, -0.4),
        (0.9, -0.3), (0.3, 0.8), (-0.5, 0.8), (-0.1, -0.99)
    ]
    colors = [
        (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5),
        (0.2, 0.7, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5), (0.1, 0.2, 0.8, 0.5),
        (0.1, 0.2, 0.8, 0.5), (0.1, 0.2, 0.8, 0.5)
    ]
    for i, color in zip(points, colors):
        gl.glColor4dv(color)
        gl.glVertex2dv(i)
    gl.glEnd()


def drawQuads():
    gl.glBegin(gl.GL_QUADS)
    quads = [
        ((-0.9, -0.8), (-0.8, -0.1), (-0.2, 0.0), (-0.1, -0.8)),
        ((0.9, -0.8), (0.8, -0.1), (0.2, 0.0), (0.1, -0.8)),
        ((-0.4, 0.8), (0.5, 0.7), (0.7, 0.2), (-0.6, 0.1)),
        ((0.1, 0.6), (-0.4, -0.4), (0.4, -0.4), (0.8, 0.1)),
    ]
    colors = [(0.9, 0.2, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5), (0.1, 0.2, 0.8, 0.5), (0.8, 0.9, 0.1, 0.5)]
    for i, color in zip(quads, colors):
        gl.glColor4dv(color)
        for p in i:
            gl.glVertex2dv(p)
    gl.glEnd()


def drawQuadStrip():
    gl.glBegin(gl.GL_QUAD_STRIP)
    quads = [
        (-0.9, -0.8), (-0.8, -0.1), (-0.1, -0.8), (-0.2, 0.0),
        (0.1, -0.8), (0.2, -0.1), (0.5, -0.8), (0.8, 0.1),
        (-0.4, 0.8), (0.5, 0.7),
    ]
    colors = [
        (0.1, 0.2, 0.8, 0.5), (0.1, 0.2, 0.8, 0.5), (0.1, 0.2, 0.8, 0.5), (0.8, 0.9, 0.1, 0.5),
        (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5),
        (0.2, 0.7, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5)
    ]
    for p, color in zip(quads, colors):
        gl.glColor4dv(color)
        gl.glVertex2dv(p)
    gl.glEnd()


def drawPolygon():
    gl.glBegin(gl.GL_POLYGON)
    points = [
        (-0.7, -0.8), (0, -0.1), (0.6, -0.6),
        (0.9, -0.0), (0.1, 0.8), (-0.5, 0.1),
    ]
    colors = [
        (0.9, 0.2, 0.1, 0.5), (0.9, 0.2, 0.1, 0.5), (0.2, 0.7, 0.1, 0.5),
        (0.2, 0.7, 0.1, 0.5), (0.1, 0.2, 0.8, 0.5), (0.1, 0.2, 0.8, 0.5),
    ]
    for i, color in zip(points, colors):
        gl.glColor4dv(color)
        gl.glVertex2dv(i)
    gl.glEnd()


# Словарь рендер-функций
renderers = dict([
    (gl.GL_POINTS, drawPoints),
    (gl.GL_LINES, drawLines),
    (gl.GL_LINE_STRIP, drawLineStrip),
    (gl.GL_LINE_LOOP, drawLineLoop),
    (gl.GL_TRIANGLES, drawTriangles),
    (gl.GL_TRIANGLE_STRIP, drawTriangleStrip),
    (gl.GL_TRIANGLE_FAN, drawTriangleFan),
    (gl.GL_QUADS, drawQuads),
    (gl.GL_QUAD_STRIP, drawQuadStrip),
    (gl.GL_POLYGON, drawPolygon),
])
