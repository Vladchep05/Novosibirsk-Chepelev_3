# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tasteDescriptionLineEdit(object):
    def setupUi(self, tasteDescriptionLineEdit):
        tasteDescriptionLineEdit.setObjectName("tasteDescriptionLineEdit")
        tasteDescriptionLineEdit.resize(554, 312)
        self.saveButton = QtWidgets.QPushButton(tasteDescriptionLineEdit)
        self.saveButton.setGeometry(QtCore.QRect(450, 260, 81, 31))
        self.saveButton.setObjectName("saveButton")
        self.nameLineEdit = QtWidgets.QLineEdit(tasteDescriptionLineEdit)
        self.nameLineEdit.setGeometry(QtCore.QRect(20, 30, 511, 20))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.roastLineEdit = QtWidgets.QLineEdit(tasteDescriptionLineEdit)
        self.roastLineEdit.setGeometry(QtCore.QRect(20, 70, 511, 20))
        self.roastLineEdit.setObjectName("roastLineEdit")
        self.typeLineEdit = QtWidgets.QLineEdit(tasteDescriptionLineEdit)
        self.typeLineEdit.setGeometry(QtCore.QRect(20, 110, 511, 20))
        self.typeLineEdit.setObjectName("typeLineEdit")
        self.descriptionLineEdit = QtWidgets.QLineEdit(tasteDescriptionLineEdit)
        self.descriptionLineEdit.setGeometry(QtCore.QRect(20, 150, 511, 20))
        self.descriptionLineEdit.setObjectName("descriptionLineEdit")
        self.priceLineEdit = QtWidgets.QLineEdit(tasteDescriptionLineEdit)
        self.priceLineEdit.setGeometry(QtCore.QRect(20, 190, 511, 20))
        self.priceLineEdit.setObjectName("priceLineEdit")
        self.volumeLineEdit = QtWidgets.QLineEdit(tasteDescriptionLineEdit)
        self.volumeLineEdit.setGeometry(QtCore.QRect(20, 230, 511, 20))
        self.volumeLineEdit.setObjectName("volumeLineEdit")
        self.label = QtWidgets.QLabel(tasteDescriptionLineEdit)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(tasteDescriptionLineEdit)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(tasteDescriptionLineEdit)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(tasteDescriptionLineEdit)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 131, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(tasteDescriptionLineEdit)
        self.label_5.setGeometry(QtCore.QRect(20, 170, 131, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(tasteDescriptionLineEdit)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 131, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(tasteDescriptionLineEdit)
        QtCore.QMetaObject.connectSlotsByName(tasteDescriptionLineEdit)

    def retranslateUi(self, tasteDescriptionLineEdit):
        _translate = QtCore.QCoreApplication.translate
        tasteDescriptionLineEdit.setWindowTitle(_translate("tasteDescriptionLineEdit", "Form"))
        self.saveButton.setText(_translate("tasteDescriptionLineEdit", "Сохранить"))
        self.label.setText(_translate("tasteDescriptionLineEdit", "Название сорта:"))
        self.label_2.setText(_translate("tasteDescriptionLineEdit", "Степень обжарки:"))
        self.label_3.setText(_translate("tasteDescriptionLineEdit", "Молотый или в зернах:"))
        self.label_4.setText(_translate("tasteDescriptionLineEdit", "Описание вкуса:"))
        self.label_5.setText(_translate("tasteDescriptionLineEdit", "Цена:"))
        self.label_6.setText(_translate("tasteDescriptionLineEdit", "Объем упаковки:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tasteDescriptionLineEdit = QtWidgets.QWidget()
    ui = Ui_tasteDescriptionLineEdit()
    ui.setupUi(tasteDescriptionLineEdit)
    tasteDescriptionLineEdit.show()
    sys.exit(app.exec_())
