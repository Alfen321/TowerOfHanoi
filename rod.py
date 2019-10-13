from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QPainter, QColor, QBrush, QPixmap
from PyQt5.QtCore import Qt, QRect, QPoint


class Rod(QWidget):
    def __init__(self, parent, x, y, disks):
        super(Rod, self).__init__(parent)
        self.setGeometry(x, y, 200, 220)
        self.disks = disks
        self.draw()

    def append(self, disk):
        self.disks.append(disk)
        self.draw()

    def pop(self):
        disk = self.disks.pop()
        self.draw()
        return disk

    def get_disks(self):
        return self.disks

    def draw(self):      
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red)
        self.setPalette(p)

        self.p = QPixmap(200, 220)
        self.p.fill(Qt.black)
        qp = QPainter()
        qp.begin(self.p)

        br = QBrush(Qt.red)  
        qp.setBrush(br)  

        qp.drawRect(90,0,20,200) # rod
        qp.drawRect(0,200,200,20) # base
        

        br = QBrush(Qt.green)  
        qp.setBrush(br)
        for index, disk in enumerate(self.disks):
            qp.drawRect((100-((disk+1)*20/2)),\
                        180-(index*20),\
                        ((disk+1)*20),\
                        20)

        qp.end()
        
        label = QLabel(self)
        label.setPixmap(self.p)
        label.show()
        self.show()