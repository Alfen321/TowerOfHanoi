import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit 
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtCore import Qt
from mainWindow import MainWindow

app = QApplication(sys.argv)

# class Main(QWidget):
#     def __init__(self):
#         super(Main, self).__init__()
#         self.initUI()
        
#     def initUI(self):      
#         self.resize(800,500)
#         self.setWindowTitle('Tower of Hanoi')
#         self.setup()
#         self.show()

#     def setup(self):
#         label = QLabel(self)
#         label.setText('Amount of blocks (from 1-9):')
#         label.setFont(QFont("Arial",14))
#         label.move(10,10)
#         label.show()

#         e1 = QLineEdit(self)
#         e1.setValidator(QIntValidator())
#         e1.setMaxLength(1)
#         e1.move(255,10)
#         e1.setFixedSize(20,30)
#         e1.setText(str(6))
#         e1.setFont(QFont("Arial",14))
#         e1.show()

#         btn = QPushButton(self)
#         btn.setText('Go!')
#         btn.setFixedSize(35,30)
#         btn.move(280,10)
#         btn.show()
#         btn.clicked.connect(self.run)
        
#     def run(self):
#         r1 = Rod(self)    


# class Rod(QWidget):
#     def __init__(self, parent):
#         super(Rod, self).__init__(parent)
#         self.initUI()
        
#     def initUI(self):      
#         self.setAutoFillBackground(True)
#         p = self.palette()
#         p.setColor(self.backgroundRole(), Qt.red)
#         self.setPalette(p)
#         self.setGeometry(300, 300, 280, 170)
#         self.b1 = QPushButton("Button", self)
#         self.b1.move(100,100)

#         self.show()



if __name__ == "__main__":
    m = MainWindow()
    sys.exit(app.exec_())
