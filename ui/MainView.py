import sys
from PyQt5 import QtWidgets

import AppLoop
import qdarkstyle
from ui.UIMainViewControl import UIMainViewControl


def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def show_main():
    app = QtWidgets.QApplication(sys.argv)
    sys._excepthook = sys.excepthook
    sys.excepthook = my_exception_hook
    AppLoop.start()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    w = UIMainViewControl()
    w.show()

    sys.exit(app.exec_())
