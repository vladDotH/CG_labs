from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel


# Виджет панели управления
class ControlPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        lt = QVBoxLayout(self)
        self.setLayout(lt)
        levelsLabel = QLabel('Количество итераций', self)
        self.iterations = QSlider(Qt.Orientation.Horizontal, self)
        radiusLabel = QLabel('Расстояние между уровнями (масштаб)', self)
        self.radius = QSlider(Qt.Orientation.Horizontal, self)

        #
        for i in [levelsLabel, self.iterations, radiusLabel, self.radius]:
            lt.addWidget(i)

        lt.addStretch()
