import sqlite3
import sys
from PyQt5 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.conn = sqlite3.connect('coffee.sqlite')
        self.cursor = self.conn.cursor()

        self.pushButton.clicked.connect(self.show_coffee_info)

        self.show()

    def show_coffee_info(self):
        query = "SELECT * FROM coffee"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        self.textBrowser.clear()

        for row in result:
            self.textBrowser.append(f"ID: {row[0]}")
            self.textBrowser.append(f"Название сорта: {row[1]}")
            self.textBrowser.append(f"Степень обжарки: {row[2]}")
            self.textBrowser.append(f"Молотый/в зернах: {row[3]}")
            self.textBrowser.append(f"Описание вкуса: {row[4]}")
            self.textBrowser.append(f"Цена: {row[5]}")
            self.textBrowser.append(f"Объем упаковки: {row[6]}")
            self.textBrowser.append("-" * 50)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
