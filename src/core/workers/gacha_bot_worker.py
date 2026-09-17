from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class GachaBotWorker(QObject):

    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel

    @pyqtSlot()
    def run(self):
        print(">>> WORKER: iniciou")
        try:
            self.viewmodel.start_bot_trap()

        except Exception as e:  # noqa: BLE001
            self.error.emit(str(e))

        finally:
            print(">>> WORKER: terminou")
            self.finished.emit()