# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\study\pyqt5\ReadCam\ReadCam.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1108, 854)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_closeWin = QtWidgets.QPushButton(Dialog)
        self.pushButton_closeWin.setGeometry(QtCore.QRect(980, 810, 93, 28))
        self.pushButton_closeWin.setObjectName("pushButton_closeWin")
        self.label_imgOri = QtWidgets.QLabel(Dialog)
        self.label_imgOri.setGeometry(QtCore.QRect(60, 270, 471, 381))
        self.label_imgOri.setObjectName("label_imgOri")
        self.label_imgPro = QtWidgets.QLabel(Dialog)
        self.label_imgPro.setGeometry(QtCore.QRect(610, 270, 471, 381))
        self.label_imgPro.setObjectName("label_imgPro")
        self.pushButton_nextImg = QtWidgets.QPushButton(Dialog)
        self.pushButton_nextImg.setGeometry(QtCore.QRect(300, 780, 145, 28))
        self.pushButton_nextImg.setObjectName("pushButton_nextImg")
        self.label_camAdr = QtWidgets.QLabel(Dialog)
        self.label_camAdr.setGeometry(QtCore.QRect(50, 30, 561, 81))
        self.label_camAdr.setObjectName("label_camAdr")
        self.pushButton_bro = QtWidgets.QPushButton(Dialog)
        self.pushButton_bro.setGeometry(QtCore.QRect(640, 40, 131, 61))
        self.pushButton_bro.setObjectName("pushButton_bro")
        self.label_playSpeed = QtWidgets.QLabel(Dialog)
        self.label_playSpeed.setGeometry(QtCore.QRect(160, 680, 61, 21))
        self.label_playSpeed.setObjectName("label_playSpeed")
        self.horizontalSlider_playSpeed = QtWidgets.QSlider(Dialog)
        self.horizontalSlider_playSpeed.setGeometry(QtCore.QRect(230, 680, 341, 22))
        self.horizontalSlider_playSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_playSpeed.setObjectName("horizontalSlider_playSpeed")

        self.retranslateUi(Dialog)
        self.pushButton_closeWin.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_closeWin.setText(_translate("Dialog", "关闭窗口"))
        self.label_imgOri.setText(_translate("Dialog", "原始图像"))
        self.label_imgPro.setText(_translate("Dialog", "处理图像"))
        self.pushButton_nextImg.setText(_translate("Dialog", "播放/暂停"))
        self.label_camAdr.setText(_translate("Dialog", "视频地址"))
        self.pushButton_bro.setText(_translate("Dialog", "浏览"))
        self.label_playSpeed.setText(_translate("Dialog", "播放速度"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

