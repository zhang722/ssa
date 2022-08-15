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

import gui.rule as rule
import subprocess


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

    subprocess.run(['/home/sen/zhangs_files/downloads/blender-3.2.0-linux-x64/blender','./render/render.blend', '-P', '~/zhangs_files/qt_ws/ssa/app.py'])

    # Start the event loop.
    app.exec()
