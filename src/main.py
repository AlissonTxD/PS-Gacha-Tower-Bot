import logging
import sys

from PyQt5.QtWidgets import QApplication

from src.views.gacha_bot_view import GachaBotView
from src.views.gt_view import GachaTower

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def start_old():
    view = GachaBotView()
    view.menu()


def start():
    app = QApplication(sys.argv)

    window = GachaTower()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
