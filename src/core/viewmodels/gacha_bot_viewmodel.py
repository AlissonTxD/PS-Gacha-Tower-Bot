import logging
from time import sleep

from src.core.config.config_controller import ConfigController
from src.core.models.crystal_cracker_model import CrystalCrackerModel
from src.core.models.gacha_model import GachaModel
from src.core.models.grinder_model import GrinderModel
from src.core.models.pego_model import PegoModel
from src.core.models.render_station_model import RenderStationModel
from src.core.models.teleport_model import TeleportModel
from src.core.models.trap_model import TrapModel


class GachaBotViewModel:
    def __init__(self):
        self.load_config()

    # Main functions
    def start_bot_trap(self) -> None:
        """
        Starts the gacha bot feeding with traps
        """
        try:
            self.load_config()
            sleep(5)
            self.render_station.leave_bed()
            self.__collect_crystals()
            self.__rest()
            while True:
                self.__feed_all_gachas()
                self.__collect_crystals()
                self.__rest(3)
        except RuntimeError as e:
            # record
            logging.warning(e)  # noqa: LOG015

    def __collect_crystals(self) -> None:
        pego = 1
        while pego <= self.qtd_pego:
            self.teleporter.teleport(f"pego{pego:02d}")
            self.pego.collect_crystals()
            self.teleporter.teleport("open crystal")
            self.cracker.crack_crystals()
            self.teleporter.teleport("grinder")
            self.grinder.grind_items()
            pego += 1

    def test_gachas(self):
        sleep(5)
        gacha = 1
        self.render_station.leave_bed()
        while gacha <= self.qtd_gacha:
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.test_gachas()
            gacha += 1

    def __feed_all_gachas(self):
        gacha = 1
        trap = 1
        while gacha <= self.qtd_gacha:
            self.teleporter.teleport(f"trap{trap:02d}")
            self.trap.get_trap()
            self.teleporter.teleport(f"gt{gacha:02d}")
            self.gacha.feed_gacha_pair_trap()
            gacha += 1
            trap += 1
            if trap > self.qtd_trap:
                trap = 1

    def __rest(self, time: float = 0):
        self.teleporter.teleport("start")
        self.render_station.join_bed()
        sleep(time)
        self.render_station.leave_bed()

    def load_config(self):
        self.config = ConfigController()
        self.general_config = self.config.load_config()
        self.qtd_gacha = self.general_config["quantities"]["gacha_boxes"]
        self.qtd_pego = self.general_config["quantities"]["pego_boxes"]
        self.qtd_trap = self.general_config["quantities"]["trap_boxes"]
        self.render_station = RenderStationModel(self.general_config)
        self.teleporter = TeleportModel(self.general_config)
        self.pego = PegoModel(self.general_config)
        self.cracker = CrystalCrackerModel(self.general_config)
        self.gacha = GachaModel(self.general_config)
        self.trap = TrapModel(self.general_config)
        self.grinder = GrinderModel(self.general_config)
