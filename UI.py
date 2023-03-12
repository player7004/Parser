import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


def createapp():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()

    app.exec()

createapp()