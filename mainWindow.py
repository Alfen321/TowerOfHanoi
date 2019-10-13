from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit 
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtCore import Qt, QTimer
from rod import Rod
from time import sleep


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):      
        self.resize(800,500)
        self.setWindowTitle('Tower of Hanoi')
        self.setup()
        self.show()

    def setup(self):
        label = QLabel(self)
        label.setText('Amount of blocks (from 1-9):')
        label.setFont(QFont("Arial",14))
        label.move(10,10)
        label.show()

        self.e1 = QLineEdit(self)
        self.e1.setValidator(QIntValidator())
        self.e1.setMaxLength(1)
        self.e1.move(255,10)
        self.e1.setFixedSize(20,30)
        self.e1.setText(str(6))
        self.e1.setFont(QFont("Arial",14))
        self.e1.show()

        btn = QPushButton(self)
        btn.setText('Go!')
        btn.setFixedSize(35,30)
        btn.move(280,10)
        btn.show()
        btn.clicked.connect(self.run)
        
    def run(self):
        amount = int(self.e1.text())
        l = [x+1 for x in range(0,amount)][::-1]
        self.rod = []
        self.rod.append(Rod(self, 10, 150, l))    
        self.rod.append(Rod(self, 260, 150, []))    
        self.rod.append(Rod(self, 510, 150, []))
        moves = self.solve(amount, 0, 1, 2)
        QTimer.singleShot(500, lambda: self.render_moves(moves))

    def render_moves(self, moves):
        move = moves[0].split('-',1)[1].split('->')
        f = int(move[0]) # from
        t = int(move[1]) # to
        self.rod[t].append(self.rod[f].pop())
        if len(moves) == 1:
            return
        QTimer.singleShot(500, lambda: self.render_moves(moves[1:]))


    def solve(self, n, f, t, a):
        '''
        n - number of disks
        f - from
        t - to
        a - auxiliary
        
        returns a string of moves to solve the puzzle
        '''
        moves = []
        if n == 1:
            return [f'{n}-{f}->{t}']
        moves.extend(self.solve(n-1,f,a,t))
        moves.append(f'{n}-{f}->{t}')
        moves.extend(self.solve(n-1,a,t,f))
        return moves