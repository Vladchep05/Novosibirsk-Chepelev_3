import sqlite3
import sys
import os
from PyQt5 import QtWidgets, QtCore
from addEditCoffeeForm import Ui_tasteDescriptionLineEdit
from dop import Ui_Form


class CoffeeApp(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.conn = sqlite3.connect(
            os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data'), 'coffee.sqlite')
        )
        self.cursor = self.conn.cursor()

        self.pushButton.clicked.connect(self.show_coffee_info)
        self.btnAddEditCoffee.clicked.connect(self.open_add_edit_window)

        self.show()

    def show_coffee_info(self):
        query = "SELECT * FROM coffee"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        self.text_browser.clear()
        for row in result:
            self.text_browser.append(f"ID: {row[0]}")
            self.text_browser.append(f"Название сорта: {row[1]}")
            self.text_browser.append(f"Степень обжарки: {row[2]}")
            self.text_browser.append(f"Молотый/в зернах: {row[3]}")
            self.text_browser.append(f"Описание вкуса: {row[4]}")
            self.text_browser.append(f"Цена: {row[5]}")
            self.text_browser.append(f"Объем упаковки: {row[6]}")
            self.text_browser.append("-" * 50)

    def open_add_edit_window(self):
        self.addEditWindow = AddEditCoffeeWindow()
        self.addEditWindow.show()


class AddEditCoffeeWindow(QtWidgets.QWidget, Ui_tasteDescriptionLineEdit):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.saveButton.clicked.connect(self.save_coffee)

    def save_coffee(self):
        name = self.nameLineEdit.text()
        roast = self.roastLineEdit.text()
        coffee_type = self.typeLineEdit.text()
        description = self.descriptionLineEdit.text()
        price = self.priceLineEdit.text()
        volume = self.volumeLineEdit.text()

        if name and roast and coffee_type and description and price and volume:
            connection = sqlite3.connect(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data'), 'coffee.sqlite')
            )
            cursor = connection.cursor()
            query = """INSERT INTO coffee (name, roast, type, description, price, volume) 
                    VALUES (?, ?, ?, ?, ?, ?)"""
            cursor.execute(query, (name, roast, coffee_type, description, price, volume))

            connection.commit()

            cursor.close()
            connection.close()

            self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
