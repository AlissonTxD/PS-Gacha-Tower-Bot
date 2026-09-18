import ctypes
import logging
from pathlib import Path

from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow

from src.core.services.window_services import WindowServices
from src.core.viewmodels.gacha_bot_viewmodel import GachaBotViewModel
from src.core.workers.gacha_bot_worker import GachaBotWorker
from src.views.gacha_tower_ui import Ui_MainWindow


class GachaTower(QMainWindow):
    def __init__(self):
        super().__init__()
        self.f10_pressed = False
        self.f10_timer = QTimer()
        self.f10_timer.timeout.connect(self.__check_f10)
        self.f10_timer.start(50)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_img_on_exe()

        self.window_services = WindowServices()
        self.gachavm = GachaBotViewModel()

        self.thread = None
        self.worker = None
        self.bot_running = False

        self.ui.btn_stop.setDisabled(True)
        self.__load_config_on_view()
        self.ui.btn_start.clicked.connect(self.start_bot)
        self.ui.btn_stop.clicked.connect(self.stop_bot)
        self.ui.btn_save.clicked.connect(self.save_config)
        self.ui.btn_calibrator.clicked.connect(self.__open_calibration_window)
        self.ui.btn_coords.clicked.connect(self.__open_color_coordinate_capture_window)

    def start_bot(self):
        if self.bot_running:
            logging.warning("Thread already running.")  # noqa: LOG015
            return
        self.window_services.focus_ark()
        self.save_config()

        self.ui.btn_start.setDisabled(True)
        self.ui.btn_stop.setEnabled(True)
        self.bot_running = True

        self.thread = QThread()
        self.worker = GachaBotWorker(self.gachavm)

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.finished.connect(self.bot_finished)

        self.worker.error.connect(self.bot_error)

        self.thread.start()

    def stop_bot(self):
        self.gachavm.stop_bot()

    def bot_finished(self):
        logging.info(">>> BOT_FINISHED: entrou")  # noqa: LOG015
        self.bot_running = False
        self.ui.btn_start.setEnabled(True)
        self.ui.btn_stop.setDisabled(True)

        logging.info(">>> BOT_FINISHED: terminou")  # noqa: LOG015

    def bot_error(self, error):
        logging.error(error)  # noqa: LOG015

    def __load_config_on_view(self):

        self.gachavm.load_config()

        config = self.gachavm.general_config

        # =========================
        # FIRST TAB - QUANTITIES
        # =========================

        self.ui.lineEdit_amount_gacha.setText(str(config["quantities"]["gacha_boxes"]))

        self.ui.lineEdit_amount_pego.setText(str(config["quantities"]["pego_boxes"]))

        self.ui.lineEdit_amount_trap.setText(str(config["quantities"]["trap_boxes"]))

        # =========================
        # SECOND TAB - CALIBRATION
        # =========================

        self.ui.lineEdit_yaw.setText(str(config["calibration"]["yaw"]))

        self.ui.lineEdit_pix_per_dregree.setText(
            str(config["calibration"]["pixel_per_degree"])
        )

        # =========================
        # TELEPORT
        # =========================

        self.ui.lineEdit_teleport_search.setText(
            self.__list_to_text(config["teleport"]["search_map"])
        )

        self.ui.lineEdit_teleport_first_on_list.setText(
            self.__list_to_text(config["teleport"]["first_on_list"])
        )

        self.ui.lineEdit_teleport_btn.setText(
            self.__list_to_text(config["teleport"]["teleport_button"])
        )

        # =========================
        # PLAYER INVENTORY
        # =========================

        self.ui.lineEdit_inventory_search.setText(
            self.__list_to_text(config["player_inventory"]["search"])
        )

        self.ui.lineEdit_inventory_transferall.setText(
            self.__list_to_text(config["player_inventory"]["transfer_all"])
        )

        self.ui.lineEdit_inventory_dropall.setText(
            self.__list_to_text(config["player_inventory"]["drop_all"])
        )

        # =========================
        # DINO INVENTORY
        # =========================

        self.ui.lineEdit_dino_search.setText(
            self.__list_to_text(config["dino_inventory"]["search"])
        )

        self.ui.lineEdit_dino_transferall.setText(
            self.__list_to_text(config["dino_inventory"]["transfer_all"])
        )

        self.ui.lineEdit_dino_dropall.setText(
            self.__list_to_text(config["dino_inventory"]["drop_all"])
        )

        self.ui.lineEdit_dino_first_slot.setText(
            self.__list_to_text(config["dino_inventory"]["first_slot"])
        )

        # =========================
        # MISC
        # =========================

        self.ui.lineEdit_tekbed_lay.setText(
            self.__list_to_text(config["misc"]["lay_on"])
        )

        self.ui.lineEdit_btn_grindall.setText(
            self.__list_to_text(config["misc"]["grind_all"])
        )

        # =========================
        # VALIDATION
        # =========================

        validation = config["validation"]

        # Inventory
        self.ui.lineEdit_v_inventory_coord.setText(
            self.__list_to_text(validation["inventory"]["position"])
        )

        self.ui.lineEdit_v_inventory_color.setText(
            self.__list_to_text(validation["inventory"]["color"])
        )

        # Teleport
        self.ui.lineEdit_v_teleport_coord.setText(
            self.__list_to_text(validation["teleport"]["position"])
        )

        self.ui.lineEdit_v_teleport_color.setText(
            self.__list_to_text(validation["teleport"]["color"])
        )

        # Tek Bed
        self.ui.lineEdit_v_tekbed_coord.setText(
            self.__list_to_text(validation["tek_bed_radial"]["position"])
        )

        self.ui.lineEdit_v_tekbed_color.setText(
            self.__list_to_text(validation["tek_bed_radial"]["color"])
        )

        # Vault
        self.ui.lineEdit_v_vault_coord.setText(
            self.__list_to_text(validation["vault_full"]["position"])
        )

        self.ui.lineEdit_v_vault_color.setText(
            self.__list_to_text(validation["vault_full"]["color"])
        )

    def __get_config_from_view(self):
        config = {
            "quantities": {
                "gacha_boxes": int(self.ui.lineEdit_amount_gacha.text()),
                "pego_boxes": int(self.ui.lineEdit_amount_pego.text()),
                "trap_boxes": int(self.ui.lineEdit_amount_trap.text()),
            },
            "calibration": {
                "pixel_per_degree": float(self.ui.lineEdit_pix_per_dregree.text()),
                "yaw": float(self.ui.lineEdit_yaw.text()),
            },
            "teleport": {
                "search_map": self.__text_to_list(
                    self.ui.lineEdit_teleport_search.text()
                ),
                "first_on_list": self.__text_to_list(
                    self.ui.lineEdit_teleport_first_on_list.text()
                ),
                "teleport_button": self.__text_to_list(
                    self.ui.lineEdit_teleport_btn.text()
                ),
            },
            "player_inventory": {
                "search": self.__text_to_list(self.ui.lineEdit_inventory_search.text()),
                "transfer_all": self.__text_to_list(
                    self.ui.lineEdit_inventory_transferall.text()
                ),
                "drop_all": self.__text_to_list(
                    self.ui.lineEdit_inventory_dropall.text()
                ),
            },
            "dino_inventory": {
                "search": self.__text_to_list(self.ui.lineEdit_dino_search.text()),
                "transfer_all": self.__text_to_list(
                    self.ui.lineEdit_dino_transferall.text()
                ),
                "drop_all": self.__text_to_list(self.ui.lineEdit_dino_dropall.text()),
                "first_slot": self.__text_to_list(
                    self.ui.lineEdit_dino_first_slot.text()
                ),
            },
            "misc": {
                "lay_on": self.__text_to_list(self.ui.lineEdit_tekbed_lay.text()),
                "grind_all": self.__text_to_list(self.ui.lineEdit_btn_grindall.text()),
            },
            "validation": {
                "inventory": {
                    "position": self.__text_to_list(
                        self.ui.lineEdit_v_inventory_coord.text()
                    ),
                    "color": self.__text_to_list(
                        self.ui.lineEdit_v_inventory_color.text()
                    ),
                },
                "teleport": {
                    "position": self.__text_to_list(
                        self.ui.lineEdit_v_teleport_coord.text()
                    ),
                    "color": self.__text_to_list(
                        self.ui.lineEdit_v_teleport_color.text()
                    ),
                },
                "tek_bed_radial": {
                    "position": self.__text_to_list(
                        self.ui.lineEdit_v_tekbed_coord.text()
                    ),
                    "color": self.__text_to_list(
                        self.ui.lineEdit_v_tekbed_color.text()
                    ),
                },
                "vault_full": {
                    "position": self.__text_to_list(
                        self.ui.lineEdit_v_vault_coord.text()
                    ),
                    "color": self.__text_to_list(self.ui.lineEdit_v_vault_color.text()),
                },
            },
        }
        return config

    def save_config(self):
        config = self.__get_config_from_view()
        self.gachavm.config.save_config(config)

    def __list_to_text(self, values):
        return ", ".join(map(str, values))

    def __text_to_list(self, text):
        return [
            float(value.strip()) if "." in value else int(value.strip())
            for value in text.split(",")
        ]

    def __open_calibration_window(self):
        self.gachavm.tools.open_calibrator()

    def __open_color_coordinate_capture_window(self):
        self.gachavm.tools.open_color_coordinate_capture()

    def __check_f10(self):

        f10_down = bool(ctypes.windll.user32.GetAsyncKeyState(0x79) & 0x8000)

        if f10_down and not self.f10_pressed:
            self.f10_pressed = True

            if self.worker:
                self.gachavm.stop_bot()

        elif not f10_down:
            self.f10_pressed = False

    def load_img_on_exe(self):
        img_path = Path(__file__).resolve().parent / "uis"

        self.ui.label_8.setPixmap(QPixmap(str(img_path / "trap100.png")))

        self.ui.label.setPixmap(QPixmap(str(img_path / "gacha100.png")))

        self.ui.fotologo.setPixmap(QPixmap(str(img_path / "ps_png.png")))

        self.ui.label_4.setPixmap(QPixmap(str(img_path / "ps_png.png")))

        self.ui.label_2.setPixmap(QPixmap(str(img_path / "pego100.png")))

        self.setWindowIcon(QIcon(str(img_path / "ps_ico.ico")))
