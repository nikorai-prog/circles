from random import randint
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_Form


class Circles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.paint)
        self.circles = []
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            x, y, w = randint(0, 450), randint(0, 300), randint(20, 100)
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            self.circles.append([x, y, w, (r, g, b)])
            qp = QPainter()
            qp.begin(self)
            self.drawer(qp)
            qp.end()
        self.do_paint = False

    def drawer(self, qp):
        for elem in self.circles:
            print(elem)
            qp.setBrush(QColor(elem[3][0], elem[3][1], elem[3][2]))
            qp.drawEllipse(elem[0], elem[1], elem[2], elem[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())