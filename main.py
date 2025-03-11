# C:\Users\User\AppData\Roaming\Python\Python311\Scripts\pyqt6-tools.exe designer
from my_window import MyWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('BMI_calculator')
    window.show()
    sys.exit(app.exec())
