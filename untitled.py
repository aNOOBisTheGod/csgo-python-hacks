import sys

from PyQt5.QtWidgets import *
from threading import Thread

from PyQt5 import QtCore, QtWidgets
from skinchanger import change_skin
from main import wh
from bhop import BunnyHop

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Ui_Dialog(Example):
    def setupUi(self, Dialog):
        self.closer = False
        self.closers = False
        self.t = Thread(target=BunnyHop)
        self.skins = Thread(target=change_skin)
        Dialog.setObjectName("Dialog")
        Dialog.resize(200, 200)
        self.cb1 = QtWidgets.QCheckBox(Dialog)
        self.cb1.setGeometry(QtCore.QRect(30, 20, 70, 17))
        self.cb1.setObjectName("cb1")
        self.cb2 = QtWidgets.QCheckBox(Dialog)
        self.cb2.setGeometry(QtCore.QRect(30, 50, 70, 17))
        self.cb2.setObjectName("cb2")
        self.cb3 = QtWidgets.QCheckBox(Dialog)
        self.cb3.setGeometry(QtCore.QRect(30, 80, 81, 17))
        self.cb3.setObjectName("cb3")
        self.cb3.stateChanged.connect(self.enablecheats)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setText("apply")
        self.pushButton.clicked.connect(self.enablecheats)
        self.pushButton.move(20, 150)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cb1.setText(_translate("Dialog", "wallhack"))
        self.cb2.setText(_translate("Dialog", "bhop"))
        self.cb3.setText(_translate("Dialog", "skinchanger"))

    def enablecheats(self):
        if self.cb2.isChecked():
            if not self.closer:
                self.closer = True
                self.t.start()
                self.t.do_run = True
        else:
            self.t.do_run = False
        if self.cb1.isChecked():
            wh(1)
        else:
            wh(2)
        if self.cb3.isChecked():
            if not self.closers:
                self.closers = True
                self.skins.start()
                self.skins.do_run = True
        else:
            self.skins.do_run = False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec())