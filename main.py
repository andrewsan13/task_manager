import sys  # нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

import application


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = application.ExampleApp()
    window.show()  # Показать окно

    app.exec_()  # запуск приложения


if __name__ == '__main__':
    main()
