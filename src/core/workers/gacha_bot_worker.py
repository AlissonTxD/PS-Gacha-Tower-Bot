from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class GachaBotWorker(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel

    @pyqtSlot()
    def run(self):
        try:
            self.viewmodel.start_bot_trap()

        except RuntimeError as e:
            self.error.emit(str(e))

        finally:
            self.finished.emit()