import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

UI_PATH = "src/views/uis/gacha_tower.ui"


class ViewMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(UI_PATH, self)


app = QApplication(sys.argv)
view = ViewMain()
view.show()
app.exec_()