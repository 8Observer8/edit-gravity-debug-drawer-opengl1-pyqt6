from PyQt6.QtCore import QSize, pyqtSignal
from PyQt6.QtWidgets import (QDoubleSpinBox, QGroupBox, QHBoxLayout,
                             QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from opengl_widget import OpenGLWidget


class MainWidget(QWidget):

    restart = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Box2D, OpenGL1, PyQt6")
        self.setFixedSize(QSize(400, 319))

        hbox = QHBoxLayout()
        openGLWidget = OpenGLWidget()
        hbox.addWidget(openGLWidget)

        groupBox = QGroupBox("Gravity")
        self.gravitySpinBox = QDoubleSpinBox(minimum=-20, maximum=-0.1,
            value=-9.8, singleStep=0.1)
        groupBoxLayout = QVBoxLayout()
        groupBoxLayout.addWidget(self.gravitySpinBox)
        groupBox.setLayout(groupBoxLayout)

        vbox = QVBoxLayout()
        vbox.addWidget(groupBox)
        btnRestart = QPushButton("Restart")
        btnRestart.clicked.connect(self.onRestartClick)
        btnRestart.setSizePolicy(QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed)
        vbox.addWidget(btnRestart)
        vbox.addStretch(1)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

        self.restart.connect(openGLWidget.restartSlot)

    def onRestartClick(self):
        self.restart.emit(self.gravitySpinBox.value())
