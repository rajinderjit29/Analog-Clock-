from PyQt5. QtWidgets import *
from PyQt5 import QtCore, QtGui 
from PyQt5. QtGui import *
from PyQt5. QtCore import *
import sys
class clock (QMainWindow):
    def __init__ (self):
        super() .__init__()
        timer = QTimer (self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle('Analog Clock')
        self.setGeometry(200, 200, 300, 300)
        self.setStyleSheet('background: black;')
        self.hpointer = QtGui.QPolygon([QPoint(6, 7), QPoint(-6, 7), QPoint(0, -50)])
        self.mPointer = QPolygon([QPoint(6, 7), QPoint(-6, 7), QPoint(0, -70)])
        self.spointer = QPolygon([QPoint(1, 1), QPoint(-1, 1), QPoint(0, -90)])
        self.bcolour = Qt.green
        self.scolour = Qt.red
    def paintEvent(self, event):
        rec = min(self.width(), self.height())
        tik = QTime.currentTime()
        painter = QPainter(self)
        def drawpointer(colour, rotation, pointer):
            painter.setBrush(QBrush(colour))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2, self.height()/2)
        painter.scale(rec/200 , rec/200)
        painter.setPen(QtCore.Qt.NoPen)
        drawpointer(self.bcolour, (30 * (tik.hour() + tik.minute() / 60)), self.hpointer)
        drawpointer(self.bcolour, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawpointer(self.scolour, (6 * tik.second()), self.spointer)
        painter.setPen(QPen(Qt.white))
        for i in range (0, 60):
            if (i % 5)==0:
                painter.drawLine(87, 0, 97, 0)
            else:
                painter.drawLine(87, 0, 92, 0)
            painter.rotate(6)
        painter.end()
if __name__ == '__main__':
    App = QApplication(sys.argv)
    win = clock()
win.show()
exit(App.exec_())