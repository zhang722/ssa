from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             QLineEdit,
                             )



class Rule(QWidget):
    def __init__(self, name, value=-1.0, subrules = [], color="lightgreen"):
        super(QWidget, self).__init__()

        layout = QVBoxLayout()

        self.name = QLabel(name)
        self.name.setStyleSheet("background-color: {}".format(color))
        self.name.setAlignment(Qt.AlignCenter)

        self.value = QLabel("init")
        self.value.setStyleSheet("background-color: white")
        self.value.setAlignment(Qt.AlignCenter)
 
        hLayoutWidget = QWidget()  
        if len(subrules):
            hLayout = QHBoxLayout()
            for rule in subrules:
                hLayout.addWidget(rule)
            hLayoutWidget.setLayout(hLayout)
          

        layout.setSpacing(0)
        layout.addWidget(self.name)
        layout.addWidget(self.value)
        layout.addWidget(hLayoutWidget)
        self.setLayout(layout)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeoutFunction)
        self.timer.start(500)
        self.time = 0

        
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getValue(self):
        return self.value.text()

    def setValue(self, value):
        self.value.setText(value)

    def timeoutFunction(self):
        self.timer.stop()
        self.time += 1
        self.setValue(str(self.time))
        self.timer.start()

