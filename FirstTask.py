# Создайте оконное приложение, отображающее карту по координатам и в масштабе, который задаётся программно.
import requests
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Умная Карта")
        self.findBt.clicked.connect(self.findf)

    def setupUi(self, SmartMap):
        SmartMap.setObjectName("SmartMap")
        SmartMap.resize(802, 800)
        self.label = QtWidgets.QLabel(SmartMap)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 801))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SmartMap)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.cordsEdit = QtWidgets.QLineEdit(SmartMap)
        self.cordsEdit.setGeometry(QtCore.QRect(30, 60, 281, 30))
        self.cordsEdit.setStyleSheet("QLineEdit#cordsEdit {\n"
                                     "    border-style: outset;\n"
                                     "    border-width: 2px;\n"
                                     "    border-radius: 10px;\n"
                                     "    border-color: beige;\n"
                                     "    font: bold 14px;\n"
                                     "    min-width: 10em;\n"
                                     "    padding: 6px;\n"
                                     "}")
        self.cordsEdit.setText("")
        self.cordsEdit.setObjectName("cordsEdit")
        self.zoomBox = QtWidgets.QSpinBox(SmartMap)
        self.zoomBox.setGeometry(QtCore.QRect(120, 105, 51, 31))
        self.zoomBox.setAutoFillBackground(False)
        self.zoomBox.setWrapping(False)
        self.zoomBox.setAccelerated(False)
        self.zoomBox.setSuffix("")
        self.zoomBox.setMaximum(21)
        self.zoomBox.setObjectName("zoomBox")
        self.label_3 = QtWidgets.QLabel(SmartMap)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(SmartMap)
        self.frame.setGeometry(QtCore.QRect(0, 0, 341, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.findBt = QtWidgets.QPushButton(SmartMap)
        self.findBt.setGeometry(QtCore.QRect(190, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.findBt.setFont(font)
        self.findBt.setStyleSheet("background-color: lightgreen")
        self.findBt.setObjectName("findBt")
        self.modeEdit = QtWidgets.QComboBox(SmartMap)
        self.modeEdit.setGeometry(QtCore.QRect(585, 60, 91, 31))
        self.modeEdit.setObjectName("modeEdit")
        self.modeEdit.addItem("")
        self.modeEdit.addItem("")
        self.modeEdit.addItem("")
        self.modeBt = QtWidgets.QPushButton(SmartMap)
        self.modeBt.setGeometry(QtCore.QRect(585, 110, 93, 28))
        self.modeBt.setObjectName("modeBt")
        self.label_4 = QtWidgets.QLabel(SmartMap)
        self.label_4.setGeometry(QtCore.QRect(505, 20, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(SmartMap)
        self.frame_2.setGeometry(QtCore.QRect(460, 0, 341, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.bynameEdit = QtWidgets.QLineEdit(SmartMap)
        self.bynameEdit.setGeometry(QtCore.QRect(30, 230, 281, 30))
        self.bynameEdit.setStyleSheet("QLineEdit#bynameEdit {\n"
                                      "    border-style: outset;\n"
                                      "    border-width: 2px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}")
        self.bynameEdit.setText("")
        self.bynameEdit.setObjectName("bynameEdit")
        self.bynameBt = QtWidgets.QPushButton(SmartMap)
        self.bynameBt.setGeometry(QtCore.QRect(40, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.bynameBt.setFont(font)
        self.bynameBt.setStyleSheet("background-color: lightgreen")
        self.bynameBt.setObjectName("bynameBt")
        self.indexBox = QtWidgets.QCheckBox(SmartMap)
        self.indexBox.setGeometry(QtCore.QRect(190, 275, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.indexBox.setFont(font)
        self.indexBox.setObjectName("indexBox")
        self.addressEdit = QtWidgets.QLineEdit(SmartMap)
        self.addressEdit.setGeometry(QtCore.QRect(339, 225, 441, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addressEdit.setFont(font)
        self.addressEdit.setStyleSheet("QLineEdit#addressEdit {\n"
                                       "    border-style: outset;\n"
                                       "    border-width: 2px;\n"
                                       "    border-radius: 10px;\n"
                                       "    border-color: beige;\n"
                                       "    font: bold 14px;\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}")
        self.addressEdit.setText("")
        self.addressEdit.setReadOnly(True)
        self.addressEdit.setObjectName("addressEdit")
        self.label_5 = QtWidgets.QLabel(SmartMap)
        self.label_5.setGeometry(QtCore.QRect(47, 185, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(SmartMap)
        self.label_6.setGeometry(QtCore.QRect(475, 185, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setScaledContents(False)
        self.label_6.setObjectName("label_6")
        self.resetBt = QtWidgets.QPushButton(SmartMap)
        self.resetBt.setGeometry(QtCore.QRect(495, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.resetBt.setFont(font)
        self.resetBt.setStyleSheet("background-color: red")
        self.resetBt.setObjectName("resetBt")
        self.frame_3 = QtWidgets.QFrame(SmartMap)
        self.frame_3.setGeometry(QtCore.QRect(0, 180, 801, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.result = QtWidgets.QLabel(SmartMap)
        self.result.setEnabled(True)
        self.result.setGeometry(QtCore.QRect(0, 330, 801, 471))
        self.result.setFrameShape(QtWidgets.QFrame.Box)
        self.result.setLineWidth(3)
        self.result.setText("")
        self.result.setScaledContents(True)
        self.result.setObjectName("result")
        self.label.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.cordsEdit.raise_()
        self.zoomBox.raise_()
        self.label_3.raise_()
        self.findBt.raise_()
        self.modeEdit.raise_()
        self.modeBt.raise_()
        self.label_4.raise_()
        self.bynameEdit.raise_()
        self.bynameBt.raise_()
        self.indexBox.raise_()
        self.addressEdit.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.resetBt.raise_()
        self.result.raise_()
        self.retranslateUi(SmartMap)
        QtCore.QMetaObject.connectSlotsByName(SmartMap)

    def retranslateUi(self, SmartMap):

        _translate = QtCore.QCoreApplication.translate
        SmartMap.setWindowTitle(_translate("SmartMap", "Умная Карта"))
        self.label_2.setText(_translate("SmartMap", "Поиск по координатам:"))
        self.label_3.setText(_translate("SmartMap", "Масштаб:"))
        self.findBt.setText(_translate("SmartMap", "НАЙТИ"))
        self.modeEdit.setItemText(0, _translate("SmartMap", "Схема"))
        self.modeEdit.setItemText(1, _translate("SmartMap", "Спутник"))
        self.modeEdit.setItemText(2, _translate("SmartMap", "Гибрид"))
        self.modeBt.setText(_translate("SmartMap", "СМЕНА"))
        self.label_4.setText(_translate("SmartMap", "Режим отображения:"))
        self.bynameBt.setText(_translate("SmartMap", "НАЙТИ"))
        self.indexBox.setText(_translate("SmartMap", "Индекс"))
        self.label_5.setText(_translate("SmartMap", "Поиск по названию:"))
        self.label_6.setText(_translate("SmartMap", "Итог поиска:"))
        self.resetBt.setText(_translate("SmartMap", "СБРОС"))

    def findf(self):
        coords = self.cordsEdit.text().replace(" ", "").split(",")
        zoom = self.zoomBox.text()
        res = requests.get(f"https://static-maps.yandex.ru/1.x/?ll={coords[1]},{coords[0]}&l=map&z={zoom}")
        if res:
            with open("output.png", "wb") as file:
                file.write(res.content)
            self.pixmap = QPixmap('output.png')
            self.result.setScaledContents(True)
            self.result.setPixmap(self.pixmap)
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
