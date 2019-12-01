from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from test import Ui_MainWindow






app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def hello():
    ui.lineEdit.setText('hello')


ui.pushButton_10.clicked.connect(hello)


sys.exit(app.exec_())