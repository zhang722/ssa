from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QPushButton,
                             QMainWindow,
                             QGridLayout,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             )

import rule


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        mainWidget = QWidget()
        
        self.origin1 = rule.Rule("速度", color="red")
        self.rule1 = rule.Rule("rule1" ,subrules=[self.origin1])
        self.rule2 = rule.Rule("rule2")
        self.rule3 = rule.Rule("rule3")
        self.rule4 = rule.Rule("rule4", subrules=[self.rule1, self.rule2, self.rule3])
        self.origin2 = rule.Rule("距离", color="red")
        self.rule5 = rule.Rule("rule5", subrules=[self.origin2])
        self.rule6 = rule.Rule("rule6", subrules=[self.rule1, self.rule2, self.rule3])
        self.rule = rule.Rule("rule4", subrules=[self.rule4, self.rule5, self.rule6])
        self.setCentralWidget(self.rule)


if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.


    # Start the event loop.
    app.exec()
