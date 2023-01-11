import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication

from main_widget import MainWidget


def main():
    QApplication.setAttribute(Qt.ApplicationAttribute.AA_UseDesktopOpenGL)
    app = QApplication(sys.argv)

    w = MainWidget()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
