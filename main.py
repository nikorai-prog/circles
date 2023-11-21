from random import choice
from random import randint
import sys
import os
import sqlite3

from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QMessageBox, QLineEdit, QInputDialog, QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.paint)
        self.circles = []
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            x, y, w = randint(0, 450), randint(0, 300), randint(20, 100)
            self.circles.append([x, y, w])
            qp = QPainter()
            qp.begin(self)
            self.drawer(qp)
            qp.end()
        self.do_paint = False

    def drawer(self, qp):
        for elem in self.circles:
            print(elem)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(elem[0], elem[1], elem[2], elem[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())