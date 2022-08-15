import sys
sys.path.append("/home/sen/zhangs_files/qt_ws/ssa")

import gui.viewer
import gui.rule
import rwriter.reader
import render.blender

import threading
from threading import Thread
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

def callback(inc, window, x_iter):
    t_now = next(x_iter)
    # window.rule.setValue(str(t_now))
    blender.assignToBlender("Cube")
    blender.update(t_now)

    t = threading.Timer(inc, callback, (inc, window, x_iter, ))
    t.start()

# def syncWindow():
#     app = QApplication([])
#     window = gui.viewer.MainWindow()
#     window.show()  # IMPORTANT!!!!! Windows are hidden by default.
#     app.exec()


if __name__=="__main__":
    # thread = Thread(target=syncWindow)
    # thread.start()

    # app = QApplication([])
    # window = gui.viewer.MainWindow()
    blender = render.blender.Blender()
    r = rwriter.reader.Reader()
    r.read("/home/sen/zhangs_files/qt_ws/ssa/rwriter/motion_path.txt")
    t_iter = iter(r.t)
    window =1
    callback(1, window, t_iter)
    # window = gui.viewer.MainWindow()
    # window.show()  # IMPORTANT!!!!! Windows are hidden by default.
    # app.exec()

