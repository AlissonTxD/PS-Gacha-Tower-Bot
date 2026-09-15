from time import sleep

from src.core.config.config_controller import ConfigController
from src.core.models.crystal_cracker_model import CrystalCracker
from src.core.models.gacha_model import GachaModel
from src.core.models.pego_model import PegoModel
from src.core.models.render_station_model import render_station_model
from src.core.models.teleport_model import TeleportModel
from src.core.models.trap_model import TrapModel
from src.core.services.ctypes_services import CtypesServices

QTD_PEGO = 12
QTD_GACHA = 40


class GachaBotViewModel:
    def __init__(self):
        self.config = ConfigController()
        self.general_config = self.config.load_config()
        self.qtd_gacha = self.general_config["quantities"]["gacha_boxes"]
        self.qtd_pego = self.general_config["quantities"]["pego_boxes"]
        self.qtd_trap = self.general_config["quantities"]["trap_boxes"]
        # self.render_station = render_station_model()
        # self.teleporter = TeleportModel()
        # self.pego = PegoModel()
        self.cracker = CrystalCracker(self.general_config)
        # self.gacha = GachaModel()
        # self.ctype = CtypesServices()
        # self.trap = TrapModel()

    # Main functions
    def start_trap(self):
        try:
            sleep(5)
            self.render_station.leave_bed_start()
            self.__collect_crystals()
            self.teleporter.teleport("start")
            self.render_station.join_bed_end()
            self.render_station.leave_bed_start()
            while True:
                self.__feed_all_gachas()
                self.__collect_crystals()
                self.teleporter.teleport("start")
                self.render_station.join_bed_end()
                sleep(3)
                self.render_station.leave_bed_start()
        except RuntimeError as e:
            self.record_replay()
            print(f"Erro salvo: {e}")

    def test_gachas(self):
        sleep(5)
        gacha = 1
        self.render_station.leave_bed_start()
        while gacha <= QTD_GACHA:
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.test_gachas()
            gacha += 1

    def __collect_crystals(self):
        pego = 1
        while pego <= QTD_PEGO:
            self.teleporter.teleport(f"pego{pego:02d}")
            self.pego.collect_crystals()
            self.teleporter.teleport("open crystal")
            self.cracker.crack_crystals()
            self.teleporter.teleport("grinder")
            self.cracker.grind_items()

    def __feed_all_gachas(self):
        gacha = 1
        trap = 1
        while gacha <= QTD_GACHA:
            self.teleporter.teleport(f"trap{trap:02d}")
            self.trap.get_trap()
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.feed_gacha_pair_trap()
            gacha += 1
            trap += 1
            if trap > 3:
                trap = 1

    def record_replay(self):
        self.ctype.key_down("leftalt")
        sleep(0.5)
        self.ctype.key_down("f10")
        sleep(0.5)
        self.ctype.key_up("f10")
        self.ctype.key_up("leftalt")
